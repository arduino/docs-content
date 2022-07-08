#!/bin/bash

# RENDER_DATASHEETS is set to true by CI
if [ -n "$RENDER_DATASHEETS" ]; then
    echo "Current system:"
    uname -a
    # Fix for SSL problem in phantom.js
    # export OPENSSL_CONF=/etc/ssl/

    mkdir /usr/share/fonts/truetype/open-sans
    mkdir /usr/share/fonts/truetype/roboto-mono

    cp -a ./styles/fonts/OpenSans*.ttf /usr/share/fonts/truetype/open-sans
    cp -a ./styles/fonts/RobotoMono*.ttf /usr/share/fonts/truetype/roboto-mono
    fc-cache /usr/share/fonts
    
    echo "Font info:"
    fc-list | grep "OpenSans"
    fc-list | grep "RobotoMono"

    apt-get -qq update -y
    # SEE: https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md#chrome-headless-doesnt-launch-on-unix
    apt-get -qq install -y -o=Dpkg::Use-Pty=0 ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils

    echo "Running on Node version: `node -v`"
    npm install
    node generate-datasheets.js
    exit 0
fi

if ! command -v node &> /dev/null
then
    echo "Please install Node.js from here https://nodejs.org/en/download/"
    exit -1
fi

VERSION=`node -v | grep -o 'v\d*'| cut -d "v" -f2`
MIN_VERSION=14

if [ $VERSION -lt $MIN_VERSION ]; then
    echo "You're using an old version of Node.js ($VERSION). Please update to $MIN_VERSION or newer."
    exit -1
fi

npm list --depth=0 > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Installing node modules..."
    npm install    
fi

npx datasheet-renderer config.json $@