# RAG System - Retrieval Augmented Generation with Groq LLM

Complete RAG (Retrieval Augmented Generation) system that processes documents, stores embeddings, and generates answers using Groq LLM.

## Features

- **Document Processing**: Support for PDF and TXT files
- **Smart Chunking**: Recursive text splitting with configurable overlap
- **Vector Store**: Local Chroma vector database with Hugging Face embeddings
- **Groq LLM Integration**: Fast and efficient answer generation
- **Interactive CLI**: User-friendly command-line interface
- **Batch Processing**: Process multiple queries efficiently
- **Statistics & Monitoring**: Track pipeline performance

## Project Structure

```
rag_system/
├── src/
│   ├── document_processor.py    # PDF/TXT document loading
│   ├── chunking.py              # Text splitting and chunking
│   ├── vector_store.py          # Chroma vector store management
│   ├── llm_groq.py              # Groq LLM interface
│   ├── rag_pipeline.py          # Complete RAG orchestration
│   └── config.py                # Configuration management
├── data/                        # Documents directory
├── vector_store/                # Local Chroma database
├── main.py                      # Interactive CLI application
├── examples.py                  # Usage examples
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
└── README.md                    # This file
```

## Installation

### 1. Clone and Navigate
```bash
cd rag_system
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
# Copy example to .env
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
```

### 5. Add Your Groq API Key
Edit `.env` file and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com

## Usage

### Interactive Mode

```bash
python main.py
```

The interactive menu provides options to:
1. Load documents from directory or single file
2. Process and chunk documents
3. Ask questions and get answers
4. View pipeline statistics
5. Reset the pipeline

### Programmatic Usage

```python
from src.config import get_config
from src.rag_pipeline import RAGPipeline

# Initialize
config = get_config()
pipeline = RAGPipeline(groq_api_key=config.GROQ_API_KEY)

# Load documents
pipeline.load_documents()

# Process (chunk and embed)
pipeline.process_documents()

# Query
result = pipeline.query("Your question here")
print(result["answer"])
```

### Examples

```bash
python examples.py
```

Includes examples for:
- Basic RAG usage
- Batch queries
- Loading specific files
- Viewing statistics

## Configuration

Edit `.env` file to customize:

```env
# Required
GROQ_API_KEY=your_key

# Optional
VECTOR_STORE_PATH=./vector_store
DOCUMENTS_PATH=./data
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
K_RETRIEVED_DOCS=5
LLM_MODEL=mixtral-8x7b-32768
LLM_TEMPERATURE=0.7
```

## Adding Documents

1. Place your PDF or TXT files in the `./data` directory
2. Or specify a custom path in the menu
3. Use the "Load documents" option in the interactive menu

Supported formats:
- `.pdf` - PDF files (with text)
- `.txt` - Plain text files

## API Reference

### RAGPipeline

```python
pipeline = RAGPipeline(
    groq_api_key="key",
    vector_store_path="./vector_store",
    documents_path="./data",
    chunk_size=1000,
    chunk_overlap=200
)

# Load documents
pipeline.load_documents(file_path=None, directory=None)

# Process and embed
pipeline.process_documents()

# Query
result = pipeline.query(question, k=5, return_source=True)

# Batch queries
results = pipeline.batch_query(questions, k=5)

# Statistics
stats = pipeline.get_pipeline_stats()
pipeline.display_stats()

# Reset
pipeline.reset_pipeline()
```

### DocumentProcessor

```python
processor = DocumentProcessor(documents_path="./data")

# Load single document
docs = processor.load_document("file.pdf")

# Load from directory
docs = processor.load_documents_from_directory()

# Load specific format
docs = processor.load_pdf("file.pdf")
docs = processor.load_txt("file.txt")
```

### TextChunker

```python
chunker = TextChunker(chunk_size=1000, chunk_overlap=200)

# Chunk documents
chunks = chunker.chunk_documents(documents)

# Chunk text
chunks = chunker.chunk_text(raw_text)

# Statistics
stats = chunker.get_chunking_stats(documents)
```

### VectorStoreManager

```python
store = VectorStoreManager(store_path="./vector_store")

# Add documents
ids = store.add_documents(documents)

# Search
results = store.search(query, k=5)

# Get stats
stats = store.get_collection_stats()

# Clear
store.clear_store()
```

### GroqLLM

```python
llm = GroqLLM(api_key="key", model="mixtral-8x7b-32768")

# Generate response
response = llm.generate_response(prompt)

# With context
response = llm.generate_response_with_context(
    prompt=question,
    context=context_text
)

# Change settings
llm.change_model("mixtral-8x7b-32768")
llm.set_temperature(0.5)
```

## How It Works

1. **Document Loading**: Loads PDF and TXT files using LangChain loaders
2. **Chunking**: Splits documents into overlapping chunks using recursive text splitting
3. **Embedding**: Converts chunks to embeddings using Hugging Face's all-MiniLM-L6-v2 model
4. **Vector Storage**: Stores embeddings in Chroma database for fast retrieval
5. **Retrieval**: Retrieves top-k most similar chunks for a given query
6. **Generation**: Uses Groq LLM to generate contextual answers

## Advanced Features

### Custom Chunking Strategies

```python
from src.chunking import CustomChunker

# Chunk by paragraphs
chunks = CustomChunker.chunk_by_paragraph(docs)

# Chunk by sentences
chunks = CustomChunker.chunk_by_sentences(docs)
```

### Similarity Threshold

```python
# Only retrieve chunks above similarity threshold
results = store.search_with_threshold(
    query=question,
    k=5,
    threshold=0.5
)
```

## Troubleshooting

### "GROQ_API_KEY not found"
- Ensure `.env` file exists and has your API key
- Check that the key is valid

### "No documents loaded"
- Place PDF/TXT files in `./data` directory
- Or specify the file path directly

### Memory issues with large documents
- Reduce chunk_size in configuration
- Process files in smaller batches

### Slow embedding generation
- First run downloads the embedding model (~30MB)
- Subsequent runs will be much faster

## Performance Tips

- **Batch size**: Default 100 documents per batch
- **Chunk size**: 1000 chars with 200 char overlap (default)
- **Model**: mixtral-8x7b-32768 is fast and accurate
- **Temperature**: Lower (0.1-0.3) for factual answers, higher (0.7-1.0) for creative

## Supported Models

Default: `mixtral-8x7b-32768`

Other available Groq models:
- `llama-2-70b-chat`
- `gemma-7b-it`
- And more...

## License

MIT License

## Support

For issues, questions, or contributions, please refer to the project documentation.
