@ECHO OFF

pip --version || pip3 --version
IF %ERRORLEVEL% NEQ 0 (
    cls
    ECHO Please install Python® from https://www.python.org/downloads/ and Pip following https://pip.pypa.io/en/stable/installation/
    EXIT /B 
)

cls
codespell --version
IF %ERRORLEVEL% NEQ 0 (
    ECHO Installing codespell
    pip install codespell || pip3 install codespell
) else (
    ECHO Codespell already installed
)
cls
codespell -I scripts/resources/spell-check-ignore-list.txt --skip="*.svg,*.dxf,*.pdf" content