@ECHO OFF

::Install fonts
copy styles\fonts %localappdata%\Microsoft\Windows\Fonts /Y
echo "Font installed on the system:"
dir %localappdata%\Microsoft\Windows\Fonts

node -v
IF %ERRORLEVEL% NEQ 0 (
    cls
    ECHO Please install Node.js from here https://nodejs.org/en/download/
    EXIT /B
) else (

    ::Only install the modules if npm list return an Error
    npm list --depth=0 || npm install && cls && ECHO Modules installed

    ::Argument %* only used with "Current directory" option
    npx datasheet-renderer config.json %*
)