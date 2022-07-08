@ECHO OFF

node -v
IF %ERRORLEVEL% NEQ 0 (
    cls
    ECHO Please install Node.js from here https://nodejs.org/en/download/
    EXIT /B 
) else (
    cls

    ::Only install the modules if npm list return an Error
    npm list --depth=0 || npm install && cls && ECHO Modules installed

    :: argument %* only used with "Current directory" option
    node generate-datasheets.js %*
)