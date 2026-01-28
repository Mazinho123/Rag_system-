# Quick Setup Guide

## ✅ What's Done

All the code is complete and dependencies are installed! Here's what you have:

1. **Complete RAG System** with:
   - PDF and TXT document processing
   - Smart text chunking
   - FAISS vector store (local, fast)
   - Groq LLM integration
   - Interactive CLI application

2. **All dependencies installed** ✓

## 🚀 Next Steps

### 1. Add Your Groq API Key

Edit the `.env` file and replace `your_groq_api_key_here` with your actual API key:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

Get your free API key from: https://console.groq.com

### 2. Add Some Documents

Put your PDF or TXT files in the `data` folder:
```
rag_system/data/
  ├── document1.pdf
  ├── document2.txt
  └── ...
```

Or use the included `sample.txt` file for testing.

### 3. Run the System

**Option A - Interactive Mode:**
```powershell
python main.py
```

Then:
1. Choose option 1 to load documents
2. Choose option 3 to process them
3. Choose option 4 to ask questions!

**Option B - Quick Start:**
```powershell
python quickstart.py
```

This will automatically test everything.

**Option C - Examples:**
```powershell
python examples.py
```

## 📝 Example Usage

```python
from src.rag_pipeline import RAGPipeline

# Initialize
pipeline = RAGPipeline(groq_api_key="your_key_here")

# Load and process documents
pipeline.load_documents()
pipeline.process_documents()

# Ask questions
result = pipeline.query("What is this document about?")
print(result["answer"])
```

## 🔧 Key Files

- `main.py` - Interactive application
- `quickstart.py` - Quick test script  
- `examples.py` - Usage examples
- `src/rag_pipeline.py` - Main RAG logic
- `.env` - Your configuration (ADD API KEY HERE!)

## ⚙️ Configuration

Edit `.env` to customize:
- `GROQ_API_KEY` - Your API key (REQUIRED)
- `CHUNK_SIZE` - Text chunk size (default: 1000)
- `K_RETRIEVED_DOCS` - Number of documents to retrieve (default: 5)
- `LLM_MODEL` - Groq model to use (default: mixtral-8x7b-32768)

## 💡 Tips

- First run downloads the embedding model (~30MB), be patient
- FAISS vector store is saved locally in `./vector_store`
- Add more documents anytime and process them
- Temperature 0.1-0.3 for factual, 0.7-1.0 for creative answers

## 🎯 That's It!

Just add your API key and you're ready to go! 🚀
