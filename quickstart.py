"""
Quick Start Script
Get started with RAG system in minutes
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import get_config
from src.rag_pipeline import RAGPipeline


def quick_start():
    """Quick start guide"""
    print("\n" + "="*60)
    print("RAG SYSTEM - QUICK START")
    print("="*60)
    
    # Step 1: Configuration
    print("\n[STEP 1] Loading configuration...")
    try:
        config = get_config()
        print("✓ Configuration loaded")
        print(f"  - API Key: {'Set ✓' if config.GROQ_API_KEY else 'NOT SET ✗'}")
        print(f"  - Documents path: {config.DOCUMENTS_PATH}")
        print(f"  - Vector store path: {config.VECTOR_STORE_PATH}")
    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        print("\n⚠️  Please set your GROQ_API_KEY in .env file")
        return
    
    # Step 2: Initialize pipeline
    print("\n[STEP 2] Initializing RAG pipeline...")
    try:
        pipeline = RAGPipeline(
            groq_api_key=config.GROQ_API_KEY,
            vector_store_path=config.VECTOR_STORE_PATH,
            documents_path=config.DOCUMENTS_PATH
        )
        print("✓ Pipeline initialized")
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    # Step 3: Load documents
    print("\n[STEP 3] Loading documents...")
    doc_count = pipeline.load_documents()
    
    if doc_count == 0:
        print("⚠️  No documents found!")
        print("   Please add PDF or TXT files to the ./data directory")
        print("   Example: Copy sample.pdf to ./data/")
        return
    
    print(f"✓ Loaded {doc_count} documents")
    
    # Step 4: Process documents
    print("\n[STEP 4] Processing documents...")
    print("   This may take a few moments for the first run...")
    chunk_count = pipeline.process_documents()
    print(f"✓ Created {chunk_count} chunks and embedded them")
    
    # Step 5: Test query
    print("\n[STEP 5] Testing with a sample query...")
    test_questions = [
        "What is the main topic?",
        "Summarize the content",
        "What are the key points?"
    ]
    
    question = test_questions[0]
    print(f"   Question: {question}")
    
    try:
        result = pipeline.query(question, k=3)
        print(f"   Answer: {result['answer'][:200]}...")
        print(f"✓ Query successful!")
    except Exception as e:
        print(f"✗ Query failed: {e}")
        return
    
    # Step 6: Success
    print("\n" + "="*60)
    print("✓ RAG SYSTEM IS READY!")
    print("="*60)
    print("\nYou can now:")
    print("1. Run 'python main.py' for interactive mode")
    print("2. Run 'python examples.py' to see more examples")
    print("3. Integrate into your own scripts")
    
    # Display statistics
    print("\n" + "-"*60)
    pipeline.display_stats()


if __name__ == "__main__":
    quick_start()
