## RAG System Setup Instructions

### Prerequisites
- Python 3.8+
- Groq API Key (free from https://console.groq.com)

### Step-by-Step Setup

#### 1. Create .env file
```bash
copy .env.example .env
```

#### 2. Add Your Groq API Key
Edit `.env` and replace `your_groq_api_key_here` with your actual API key from https://console.groq.com

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- langchain & langchain-community (LLM framework)
- langchain-groq (Groq integration)
- chromadb (Vector store)
- pypdf (PDF processing)
- sentence-transformers (Embeddings)
- python-dotenv (Environment variables)

#### 4. Add Your Documents
Place PDF or TXT files in the `./data` directory:
```
rag_system/data/
  ├── document1.pdf
  ├── document2.txt
  └── ...
```

#### 5. Run Quick Start
```bash
python quickstart.py
```

This will verify your setup and test the system.

### Usage

#### Interactive Mode
```bash
python main.py
```

Menu options:
1. Load documents
2. Process documents
3. Ask questions
4. View statistics
5. Reset pipeline

#### Examples
```bash
python examples.py
```

#### Advanced Examples
```bash
python advanced_examples.py
```

### Troubleshooting

**Error: "GROQ_API_KEY not found"**
- Ensure .env file exists in the rag_system directory
- Check that the API key is correctly set
- Restart the application

**Error: "No documents loaded"**
- Place PDF or TXT files in ./data directory
- Ensure files are readable
- Check file paths in configuration

**ImportError: "No module named 'langchain'"**
```bash
pip install -r requirements.txt
```

**Slow first run**
- First execution downloads the embedding model (~30MB)
- Subsequent runs will be much faster

### Configuration File (.env)

```env
# Required
GROQ_API_KEY=your_api_key

# Optional (defaults shown)
VECTOR_STORE_PATH=./vector_store
DOCUMENTS_PATH=./data
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
K_RETRIEVED_DOCS=5
LLM_MODEL=mixtral-8x7b-32768
LLM_TEMPERATURE=0.7
```

### Project Files

- `main.py` - Interactive CLI application
- `examples.py` - Usage examples
- `advanced_examples.py` - Advanced features
- `quickstart.py` - Quick start guide
- `requirements.txt` - Python dependencies
- `.env.example` - Environment template
- `data/` - Documents directory
- `vector_store/` - Local database (created automatically)
- `src/` - Core modules

### Core Modules

- `src/document_processor.py` - Load PDF/TXT files
- `src/chunking.py` - Text splitting and chunking
- `src/vector_store.py` - Chroma database management
- `src/llm_groq.py` - Groq LLM interface
- `src/rag_pipeline.py` - Complete RAG pipeline
- `src/config.py` - Configuration management

### Next Steps

1. ✅ Follow setup steps above
2. ✅ Run `python quickstart.py`
3. ✅ Add your documents to `./data`
4. ✅ Run `python main.py` for interactive mode
5. ✅ Ask questions about your documents

### Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review examples in examples.py
3. Check environment variables in .env
4. Ensure Groq API key is valid

### Groq API Key

Get your free API key:
1. Go to https://console.groq.com
2. Sign up or log in
3. Create a new API key
4. Add it to your .env file

Groq provides:
- Free API access
- Fast LLM inference
- Multiple model options
- Generous rate limits
