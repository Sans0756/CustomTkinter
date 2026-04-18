@echo off
echo Setting up CustomTkinter + GPT4All Example for Windows...

echo.
REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
REM Upgrade pip to the latest version
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Error: Failed to upgrade pip.
    pause
    exit /b 1
)

echo.
REM Install CustomTkinter from the local repository
echo Installing CustomTkinter...
python -m pip install -e .
if errorlevel 1 (
    echo Error: Failed to install CustomTkinter.
    pause
    exit /b 1
)

echo.
REM Install GPT4All Python package
echo Installing GPT4All...
python -m pip install gpt4all
if errorlevel 1 (
    echo Error: Failed to install GPT4All.
    pause
    exit /b 1
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Run the example app:
echo    python examples\gpt4all_example.py
echo 2. Wait for the GPT4All model to download on first run.
echo 3. Start chatting with the local AI.
echo.
pause