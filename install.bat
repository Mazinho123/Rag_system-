@echo off
REM Installation and Setup Script for RAG System (Windows)

echo ======================================
echo RAG SYSTEM - INSTALLATION SCRIPT
echo ======================================
echo.

REM Check Python version
echo [1] Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo X Python not found. Please install Python 3.8+
    pause
    exit /b 1
)
echo OK Python available
echo.

REM Create virtual environment (optional)
echo [2] Creating virtual environment...
python -m venv venv
if %errorlevel% equ 0 (
    echo OK Virtual environment created
    echo    Activate with: venv\Scripts\activate
) else (
    echo WARNING Could not create virtual environment, continuing...
)
echo.

REM Install dependencies
echo [3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo X Error installing dependencies
    pause
    exit /b 1
)
echo OK Dependencies installed
echo.

REM Setup environment file
echo [4] Setting up environment configuration...
if not exist .env (
    copy .env.example .env
    echo OK Created .env file from .env.example
    echo    WARNING IMPORTANT: Edit .env and add your GROQ_API_KEY
) else (
    echo OK .env file already exists
)
echo.

REM Create data directory
echo [5] Creating data directory...
if not exist data mkdir data
echo OK Data directory ready at .\data
echo.

REM Create vector_store directory
echo [6] Creating vector store directory...
if not exist vector_store mkdir vector_store
echo OK Vector store directory ready at .\vector_store
echo.

echo ======================================
echo OK INSTALLATION COMPLETE!
echo ======================================
echo.
echo NEXT STEPS:
echo 1. Edit .env file and add your GROQ_API_KEY
echo 2. Place your PDF/TXT files in the .\data directory
echo 3. Run: python quickstart.py
echo 4. Or run: python main.py for interactive mode
echo.
pause
