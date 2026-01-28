#!/bin/bash
# Installation and Setup Script for RAG System

echo "======================================"
echo "RAG SYSTEM - INSTALLATION SCRIPT"
echo "======================================"
echo ""

# Check Python version
echo "[1] Checking Python version..."
python --version
if [ $? -ne 0 ]; then
    echo "✗ Python not found. Please install Python 3.8+"
    exit 1
fi
echo "✓ Python available"
echo ""

# Create virtual environment (optional)
echo "[2] Creating virtual environment..."
python -m venv venv
if [ $? -eq 0 ]; then
    echo "✓ Virtual environment created"
    echo "   Activate with: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)"
else
    echo "⚠ Could not create virtual environment, continuing..."
fi
echo ""

# Install dependencies
echo "[3] Installing dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed"
else
    echo "✗ Error installing dependencies"
    exit 1
fi
echo ""

# Setup environment file
echo "[4] Setting up environment configuration..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file from .env.example"
    echo "  ⚠ IMPORTANT: Edit .env and add your GROQ_API_KEY"
else
    echo "✓ .env file already exists"
fi
echo ""

# Create data directory
echo "[5] Creating data directory..."
mkdir -p data
echo "✓ Data directory ready at ./data"
echo ""

# Create vector_store directory
echo "[6] Creating vector store directory..."
mkdir -p vector_store
echo "✓ Vector store directory ready at ./vector_store"
echo ""

echo "======================================"
echo "✓ INSTALLATION COMPLETE!"
echo "======================================"
echo ""
echo "NEXT STEPS:"
echo "1. Edit .env file and add your GROQ_API_KEY"
echo "2. Place your PDF/TXT files in the ./data directory"
echo "3. Run: python quickstart.py"
echo "4. Or run: python main.py for interactive mode"
echo ""
