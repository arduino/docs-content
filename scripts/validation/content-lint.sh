#!/bin/bash

if ! command -v node &> /dev/null
then
    echo "Please install Node.js from here https://nodejs.org/en/download/"
    exit
fi

npm list --depth=0 > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Installing node modules..."
    npm install    
fi

node validate.js "$@"