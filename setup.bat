@echo off
REM ============================================================================
REM Quick Setup Script for Forensic Analysis Tool (Windows)
REM ============================================================================

echo.
echo ========================================
echo Forensic Analysis Tool - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Python found
python --version

REM Create virtual environment
echo [2/4] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
echo [3/4] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo [4/4] Installing dependencies...
pip install -r requirements.txt --quiet

REM Download TextBlob corpora
echo.
echo Downloading TextBlob corpora (required for sentiment analysis)...
python -m textblob.download_corpora

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the tool:
echo   1. Activate venv: venv\Scripts\activate.bat
echo   2. Run: python forensic_analyzer.py incident_log.csv
echo.
echo Or simply run: python forensic_analyzer.py
echo.
pause
