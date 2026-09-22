import unittest
import tempfile
import os
import shutil
import sys

# Add repo root to sys.path so scripts can be imported
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.validation.image_links.image_links import (
    validate_missing,
    get_all_assets,
    IGNORE_CACHE,
    ASSET_IGNORE_CACHE,
)
from scripts.validation.relative_links.relative_links import (
    validate_file,
    map_file_to_url,
    is_ignored,
    IGNORE_CACHE as REL_IGNORE_CACHE,
)


class TestImageLinksIgnoreDecoupling(unittest.TestCase):
    def setUp(self):
        IGNORE_CACHE.clear()
        ASSET_IGNORE_CACHE.clear()
        self.test_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.test_dir, 'content')
        os.makedirs(self.content_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        IGNORE_CACHE.clear()
        ASSET_IGNORE_CACHE.clear()

    def test_ignored_markdown_file_indexes_images_and_prevents_orphan_false_positive(self):
        """
        PAT-23 Part 1: If an ignored markdown file references an image in a shared
        non-ignored assets directory, that image must be added to referenced_images
        so get_all_assets() does not flag it as an orphaned unlinked asset.
        """
        # Create non-ignored assets directory with an image
        assets_dir = os.path.join(self.content_dir, 'shared', 'assets')
        os.makedirs(assets_dir)
        img_path = os.path.join(assets_dir, 'statusbar-terminal-hl.png')
        with open(img_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')

        # Create ignored subdirectory with a markdown file referencing the image
        ignored_sub = os.path.join(self.content_dir, 'software', 'app-lab', 'cli')
        os.makedirs(ignored_sub)
        with open(os.path.join(self.content_dir, 'software', 'app-lab', '.lintignore'), 'w') as f:
            f.write('cli/\n')

        md_file = os.path.join(ignored_sub, 'guide.md')
        rel_img = os.path.relpath(img_path, ignored_sub).replace('\\', '/')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f'# App Lab CLI\n\n![Screenshot]({rel_img})\n')

        # Validate
        missing, referenced = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        assets = get_all_assets(self.content_dir, self.test_dir)
        unlinked = assets - referenced

        self.assertIn(os.path.normpath(img_path), referenced)
        self.assertEqual(len(unlinked), 0)
        self.assertEqual(len(missing), 0)

    def test_broken_image_in_ignored_file_is_suppressed(self):
        """
        Missing images in ignored markdown files should not be reported in missing_images.
        """
        ignored_sub = os.path.join(self.content_dir, 'ignored_section')
        os.makedirs(ignored_sub)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('ignored_section/\n')

        with open(os.path.join(ignored_sub, 'page.md'), 'w', encoding='utf-8') as f:
            f.write('![Nonexistent](missing-image.png)\n')

        missing, _ = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        self.assertEqual(len(missing), 0)

    def test_broken_image_in_unignored_file_is_reported(self):
        """
        Missing images in active (non-ignored) markdown files must be flagged.
        """
        valid_dir = os.path.join(self.content_dir, 'active_section')
        os.makedirs(valid_dir)
        with open(os.path.join(valid_dir, 'page.md'), 'w', encoding='utf-8') as f:
            f.write('![Nonexistent](missing-image.png)\n')

        missing, _ = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        self.assertEqual(len(missing), 1)

    def test_genuinely_unlinked_asset_is_detected(self):
        """
        Assets never referenced by ANY markdown file must still be flagged as unlinked.
        """
        assets_dir = os.path.join(self.content_dir, 'assets')
        os.makedirs(assets_dir)
        orphan_path = os.path.join(assets_dir, 'orphan.png')
        with open(orphan_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')

        _, referenced = validate_missing(self.content_dir, self.test_dir, content_dir=self.content_dir)
        assets = get_all_assets(self.content_dir, self.test_dir)
        unlinked = assets - referenced
        self.assertEqual(unlinked, {os.path.normpath(orphan_path)})


class TestRelativeLinksIgnoreDecoupling(unittest.TestCase):
    def setUp(self):
        REL_IGNORE_CACHE.clear()
        self.test_dir = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.test_dir, 'content')
        os.makedirs(self.content_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        REL_IGNORE_CACHE.clear()

    def test_unignored_page_can_link_to_ignored_page(self):
        """
        PAT-23 Part 2: Markdown files in ignored directories still build production routes.
        When indexing valid_production_paths, all .md files must be included so active
        articles can link to them without false-positive Broken Link errors.
        """
        # Create ignored legacy hardware section
        legacy_dir = os.path.join(self.content_dir, 'hardware', 'legacy-mkr')
        os.makedirs(legacy_dir)
        with open(os.path.join(self.content_dir, '.lintignore'), 'w') as f:
            f.write('hardware/legacy-mkr\n')

        with open(os.path.join(legacy_dir, 'mkr-zero.md'), 'w', encoding='utf-8') as f:
            f.write('# MKR Zero\n\nSome pinout information.\n')

        # Create active unignored section linking to the legacy section
        active_dir = os.path.join(self.content_dir, 'software', 'app-lab')
        os.makedirs(active_dir)
        active_file = os.path.join(active_dir, 'getting-started.md')
        with open(active_file, 'w', encoding='utf-8') as f:
            f.write('# Getting Started\n\nCheck out [MKR Zero](/hardware/legacy-mkr/) for hardware details.\n')

        # Build route map as validate does
        valid_production_paths = {}
        for root, _, files in os.walk(self.content_dir):
            for file in files:
                if file.endswith('.md'):
                    f_path = os.path.join(root, file)
                    url = map_file_to_url(f_path, self.content_dir)
                    if url not in valid_production_paths:
                        valid_production_paths[url] = []
                    valid_production_paths[url].append(f_path)

        # Validate active file
        anchor_cache = {}
        issues = validate_file(active_file, valid_production_paths, self.content_dir, anchor_cache)
        self.assertEqual(issues, [])

    def test_broken_link_to_nonexistent_page_is_still_flagged(self):
        """
        Links that actually resolve nowhere must still be reported as broken.
        """
        active_dir = os.path.join(self.content_dir, 'software')
        os.makedirs(active_dir)
        active_file = os.path.join(active_dir, 'intro.md')
        with open(active_file, 'w', encoding='utf-8') as f:
            f.write('# Intro\n\n[Broken Link](/does/not/exist/)\n')

        valid_production_paths = {}
        for root, _, files in os.walk(self.content_dir):
            for file in files:
                if file.endswith('.md'):
                    f_path = os.path.join(root, file)
                    url = map_file_to_url(f_path, self.content_dir)
                    if url not in valid_production_paths:
                        valid_production_paths[url] = []
                    valid_production_paths[url].append(f_path)

        anchor_cache = {}
        issues = validate_file(active_file, valid_production_paths, self.content_dir, anchor_cache)
        self.assertEqual(len(issues), 1)
        self.assertIn("Broken link", issues[0])

    def test_multi_file_route_anchor_validation(self):
        """
        Pages comprised of multiple markdown files (overview.md, tech-specs.md, etc.)
        should allow anchors defined in any of the contributing files.
        """
        board_dir = os.path.join(self.content_dir, 'hardware', 'uno-q')
        os.makedirs(board_dir)

        # File 1: overview
        with open(os.path.join(board_dir, 'overview.md'), 'w', encoding='utf-8') as f:
            f.write('# Overview\n\n## Pinout\nPinout details here.\n')

        # File 2: tech-specs
        with open(os.path.join(board_dir, 'tech-specs.md'), 'w', encoding='utf-8') as f:
            f.write('# Tech Specs\n\n## Power Ratings\nPower details.\n')

        # File 3: active tutorial linking to #pinout
        tut_dir = os.path.join(self.content_dir, 'tutorials')
        os.makedirs(tut_dir)
        tut_file = os.path.join(tut_dir, 'guide.md')
        with open(tut_file, 'w', encoding='utf-8') as f:
            f.write('# Guide\n\nSee [Uno Q Pinout](/hardware/uno-q/#pinout).\n')

        valid_production_paths = {}
        for root, _, files in os.walk(self.content_dir):
            for file in files:
                if file.endswith('.md'):
                    f_path = os.path.join(root, file)
                    url = map_file_to_url(f_path, self.content_dir)
                    if url not in valid_production_paths:
                        valid_production_paths[url] = []
                    valid_production_paths[url].append(f_path)

        anchor_cache = {}
        issues = validate_file(tut_file, valid_production_paths, self.content_dir, anchor_cache)
        self.assertEqual(issues, [])


if __name__ == '__main__':
    unittest.main()
