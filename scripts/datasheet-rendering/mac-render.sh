#!/bin/bash

FONT_DIR="$HOME/Library/Fonts"

if [ -z "$CI" ]; then
    echo "Analyzing local macOS environment..."
else
    echo "Running in CI mode on macOS"
fi

echo "Configuring fonts..."
mkdir -p "$FONT_DIR"

cp ./styles/fonts/OpenSans*.ttf "$FONT_DIR/" 2>/dev/null
cp ./styles/fonts/RobotoMono*.ttf "$FONT_DIR/" 2>/dev/null
cp ./styles/fonts/NotoSansSC*.ttf "$FONT_DIR/" 2>/dev/null
cp ./styles/fonts/NotoSansTC*.ttf "$FONT_DIR/" 2>/dev/null

if command -v fc-cache &> /dev/null; then
    fc-cache -f -v
fi

if ! command -v node &> /dev/null; then
    echo "Node.js not found. Please install it with: brew install node"
    exit 1
fi

NODE_VERSION=$(node -v | grep -oE '[0-9]+' | head -n 1)
if [ "$NODE_VERSION" -lt 14 ]; then
    echo "Node.js version is too old ($NODE_VERSION). Update required."
    exit 1
fi

if [ ! -d "node_modules" ]; then
    echo "node_modules folder not found. Installing dependencies..."
    npm install
fi

# Set Puppeteer to use the installed Chrome browser
export PUPPETEER_EXECUTABLE_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
export PUPPETEER_SKIP_DOWNLOAD=true

echo "Starting rendering..."
# Render the default (English) datasheets plus every localized config (config.<lang>.json).
# Configs whose source files don't exist are skipped: each run costs a tree walk and a browser launch.
SEARCH_PATH="${1:-../../content/hardware}"
for config in config.json config.*.json; do
    [ -e "$config" ] || continue
    if [ "$config" != "config.json" ]; then
        PATTERN=$(node -p "JSON.parse(require('fs').readFileSync('$config','utf8')).datasheetFile[0]" 2>/dev/null)
        if [ -z "$(find "$SEARCH_PATH" -name "$PATTERN" -print -quit 2>/dev/null)" ]; then
            echo "⏭  Skipping $config (no matching datasheet files)"
            continue
        fi
    fi
    echo "▶ Rendering datasheets with $config ..."
    npx datasheet-renderer "$config" "$@"
done