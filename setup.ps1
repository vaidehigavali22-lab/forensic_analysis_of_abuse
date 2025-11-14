# ============================================================================
# Quick Setup Script for Forensic Analysis Tool (PowerShell)
# ============================================================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Forensic Analysis Tool - Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[1/4] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://www.python.org" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit
}

# Create virtual environment
Write-Host "[2/4] Creating/checking virtual environment..." -ForegroundColor Yellow
if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "Virtual environment already exists" -ForegroundColor Gray
}

# Activate virtual environment
Write-Host "[3/4] Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "[4/4] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet

# Download TextBlob corpora
Write-Host ""
Write-Host "Downloading TextBlob corpora (required for sentiment analysis)..." -ForegroundColor Yellow
python -m textblob.download_corpora

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To run the tool:" -ForegroundColor Cyan
Write-Host "  1. Activate venv: .\venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "  2. Run: python forensic_analyzer.py incident_log.csv" -ForegroundColor Gray
Write-Host ""
Write-Host "Or simply run: python forensic_analyzer.py" -ForegroundColor Gray
Write-Host ""
