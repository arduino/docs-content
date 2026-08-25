import os
import yaml
import re

# --- Configuration ---
MODELS_YAML = "../app-bricks-py/models/models-list.yaml"

# The HTML comments to look for in your Markdown files
START_MARKER = "<!-- app-lab-models table start -->"
END_MARKER = "<!-- app-lab-models table end -->"

BRICK_MAPPING = {
    'arduino:gesture_recognition': {'task': 'Gesture recognition', 'family': 'vision'},
    'arduino:image_classification': {'task': 'Image classification', 'family': 'vision'},
    'arduino:video_image_classification': {'task': 'Image classification', 'family': 'vision'},
    'arduino:object_detection': {'task': 'Object detection', 'family': 'vision'},
    'arduino:video_object_detection': {'task': 'Object detection', 'family': 'vision'},
    'arduino:visual_anomaly_detection': {'task': 'Visual anomaly detection', 'family': 'vision'},
    'arduino:pose_estimation': {'task': 'Pose estimation', 'family': 'vision'},
    'arduino:audio_classification': {'task': 'Audio classification', 'family': 'audio'},
    'arduino:keyword_spotting': {'task': 'Keyword spotting', 'family': 'audio'},
    'arduino:asr': {'task': 'Speech to text', 'family': 'audio'},
    'arduino:tts': {'task': 'Text to speech', 'family': 'audio'},
    'arduino:llm': {'task': 'Language model', 'family': 'language'},
    'arduino:vlm': {'task': 'Vision-language model', 'family': 'language'},
    'arduino:motion_detection': {'task': 'Motion detection', 'family': 'sensor'},
    'arduino:vibration_anomaly_detection': {'task': 'Vibration anomaly detection', 'family': 'sensor'}
}

FAMILY_BLURBS = {
    'vision': {
        'title': 'Vision',
        'desc': 'Camera-in models: detection, classification and anomaly spotting over image or video streams.'
    },
    'audio': {
        'title': 'Audio & speech',
        'desc': 'Microphone-in models: wake words, sound classification, transcription and synthesis.'
    },
    'language': {
        'title': 'Language',
        'desc': 'Generative models running on-device through Genie or llama.cpp.'
    },
    'sensor': {
        'title': 'Sensor',
        'desc': 'Models over accelerometer and vibration data, no camera or microphone required.'
    }
}

BOARD_MAPPING = {
    'unoq': 'UNO Q',
    'ventunoq': 'VENTUNO Q'
}

SOURCE_MAPPING = {
    'edgeimpulse': 'Edge Impulse',
    'qualcomm-ai-hub': 'Qualcomm AI Hub',
    'huggingface': 'Hugging Face'
}

FAMILIES_ORDER = ['vision', 'audio', 'language', 'sensor']

def format_size(size_mb):
    if size_mb is None:
        return "—"
    if size_mb >= 1000:
        return f"{size_mb / 1024:.2f}GB"
    return f"{size_mb}MB"

def build_markdown_table():
    """Reads models-list.yaml and builds the Markdown tables."""
    if not os.path.exists(MODELS_YAML):
        print(f"Error: File '{MODELS_YAML}' not found.")
        return None

    try:
        with open(MODELS_YAML, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Failed to process {MODELS_YAML}: {e}")
        return None

    models_list = data.get('models', [])
    parsed_models = []

    for model_dict in models_list:
        for key, model in model_dict.items():
            name = model.get('name', key)
            bricks = [b.get('id') for b in model.get('bricks', []) if b.get('id')]
            
            task = model.get('task')
            family = model.get('family')
            if not task or not family:
                for b in bricks:
                    if b in BRICK_MAPPING:
                        task = task or BRICK_MAPPING[b]['task']
                        family = family or BRICK_MAPPING[b]['family']
                        break
            if not task or not family:
                raise ValueError(f"Could not determine task/family for model '{key}'.")
            
            raw_boards = model.get('supported_boards', [])
            boards = []
            for b in raw_boards:
                if b not in BOARD_MAPPING:
                    raise ValueError(f"Unknown board identifier '{b}' on model '{key}'. Please update BOARD_MAPPING.")
                boards.append(BOARD_MAPPING[b])
            boards_str = ", ".join(boards) if boards else "Unrestricted"
            
            meta = model.get('metadata', {})
            raw_source = meta.get('source')
            if raw_source:
                if raw_source not in SOURCE_MAPPING:
                    raise ValueError(f"Unknown source identifier '{raw_source}' on model '{key}'. Please update SOURCE_MAPPING.")
                source_name = SOURCE_MAPPING[raw_source]
            else:
                source_name = '—'
            
            src_url = meta.get('source-model-url') or meta.get('ei-model-url')
            if src_url and source_name != '—':
                source_linked = f"[{source_name}]({src_url})"
            else:
                source_linked = source_name
            
            description = model.get('description', '')
            if isinstance(description, str):
                description = description.replace('\n', ' ').strip()
            
            parsed_models.append({
                'name': name,
                'family': family,
                'boards': boards_str,
                'description': description,
                'source': source_linked
            })

    # Group by family
    family_groups = {f: [] for f in FAMILIES_ORDER}
    for m in parsed_models:
        if m['family'] in family_groups:
            family_groups[m['family']].append(m)
        else:
            if 'Unknown' not in family_groups:
                family_groups['Unknown'] = []
            family_groups['Unknown'].append(m)

    output = []
    
    for fam in FAMILIES_ORDER + ['Unknown']:
        models_in_fam = family_groups.get(fam, [])
        if not models_in_fam:
            continue
            
        if fam in FAMILY_BLURBS:
            title = FAMILY_BLURBS[fam]['title']
            desc = FAMILY_BLURBS[fam]['desc']
            output.append(f"### {title}")
            output.append("")
            output.append(desc)
            output.append("")
        else:
            output.append(f"### {fam}")
            output.append("")
            
        output.append("| Model | Boards | Description | Source |")
        output.append("| :--- | :--- | :--- | :--- |")
        
        # Sort models in family
        models_in_fam.sort(key=lambda x: x['name'].lower())
        
        for m in models_in_fam:
            output.append(f"| {m['name']} | {m['boards']} | {m['description']} | {m['source']} |")
            
        output.append("")

    while output and output[-1] == "":
        output.pop()

    return "\n".join(output)

def inject_table_into_markdown(table_content):
    """Finds Markdown files with the appropriate wrappers and updates them."""
    if not table_content:
        return
        
    pattern = re.compile(rf"({START_MARKER}\n).*?(\n{END_MARKER})", re.DOTALL)
    
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if START_MARKER in content and END_MARKER in content:
                    updated_content = pattern.sub(rf"\1{table_content}\2", content)
                    
                    if content != updated_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"✅ Successfully updated table in: {filepath}")
                    else:
                        print(f"⚡ No changes needed for: {filepath} (Table is up to date)")

if __name__ == "__main__":
    print("Generating Models Markdown Table...")
    md_table = build_markdown_table()
    
    if md_table:
        print("Scanning Markdown files for injection markers...")
        inject_table_into_markdown(md_table)
        print("Done!")
