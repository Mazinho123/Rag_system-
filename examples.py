"""
Example usage of RAG Pipeline
Demonstrates how to use the RAG system programmatically
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import get_config
from src.rag_pipeline import RAGPipeline


def example_basic_usage():
    """Example: Basic RAG usage"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic RAG Usage")
    print("="*60)
    
    # Load configuration
    config = get_config()
    
    # Initialize pipeline
    pipeline = RAGPipeline(
        groq_api_key=config.GROQ_API_KEY,
        vector_store_path=config.VECTOR_STORE_PATH,
        documents_path=config.DOCUMENTS_PATH
    )
    
    # Load documents
    print("\n1. Loading documents...")
    doc_count = pipeline.load_documents()
    print(f"   Loaded {doc_count} documents")
    
    if doc_count == 0:
        print("   ⚠️  No documents found. Please add PDF/TXT files to ./data directory")
        return
    
    # Process documents
    print("\n2. Processing documents...")
    chunk_count = pipeline.process_documents()
    print(f"   Created {chunk_count} chunks")
    
    # Query
    print("\n3. Querying...")
    question = "What is the main topic of the document?"
    result = pipeline.query(question)
    
    print(f"\n   Question: {result['question']}")
    print(f"   Answer: {result['answer'][:300]}...")
    print(f"   Sources used: {result['num_sources']}")


def example_batch_queries():
    """Example: Batch queries"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Batch Queries")
    print("="*60)
    
    config = get_config()
    pipeline = RAGPipeline(groq_api_key=config.GROQ_API_KEY)
    
    # Load and process
    pipeline.load_documents()
    pipeline.process_documents()
    
    # Batch queries
    questions = [
        "What are the key points?",
        "Summarize the content",
        "What is the conclusion?"
    ]
    
    results = pipeline.batch_query(questions)
    
    for i, result in enumerate(results, 1):
        print(f"\n[{i}] {result['question']}")
        print(f"    {result['answer'][:150]}...")


def example_with_specific_file():
    """Example: Load specific file"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Load Specific File")
    print("="*60)
    
    config = get_config()
    pipeline = RAGPipeline(groq_api_key=config.GROQ_API_KEY)
    
    # Load specific file
    file_path = "./data/sample.pdf"  # Change to your file
    print(f"\nLoading {file_path}...")
    doc_count = pipeline.load_documents(file_path=file_path)
    
    if doc_count > 0:
        pipeline.process_documents()
        
        # Query
        result = pipeline.query("Summarize this document")
        print(f"\nSummary: {result['answer'][:500]}...")
    else:
        print(f"File not found: {file_path}")


def example_statistics():
    """Example: View statistics"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Pipeline Statistics")
    print("="*60)
    
    config = get_config()
    pipeline = RAGPipeline(groq_api_key=config.GROQ_API_KEY)
    
    # Load and process
    pipeline.load_documents()
    pipeline.process_documents()
    
    # Display stats
    pipeline.display_stats()
    
    stats = pipeline.get_pipeline_stats()
    print("Chunking Details:")
    print(f"  Average chunk size: {stats['chunking_stats']['average_chunk_size']:.0f} characters")
    print(f"  Total characters: {stats['chunking_stats']['total_characters']}")


def main():
    """Run examples"""
    print("\n" + "="*60)
    print("RAG SYSTEM - EXAMPLES")
    print("="*60)
    print("\nChoose an example to run:")
    print("1. Basic RAG usage")
    print("2. Batch queries")
    print("3. Load specific file")
    print("4. View statistics")
    print("0. Exit")
    
    choice = input("\nEnter choice: ").strip()
    
    try:
        if choice == "1":
            example_basic_usage()
        elif choice == "2":
            example_batch_queries()
        elif choice == "3":
            example_with_specific_file()
        elif choice == "4":
            example_statistics()
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
