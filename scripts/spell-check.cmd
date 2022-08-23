@ECHO OFF

codespell --version
IF %ERRORLEVEL% NEQ 0 (
    ECHO Installing codespell
    pip install codespell || pip3 install codespell
) else (
    ECHO Codespell already installed
)
cls
codespell -I scripts/resources/spell-check-ignore-list.txt --skip="*.svg,*.dxf" content
ECHO Spell-check finished