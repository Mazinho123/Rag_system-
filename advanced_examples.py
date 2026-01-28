"""
Advanced Configuration Example
Shows how to customize the RAG system
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.document_processor import DocumentProcessor
from src.chunking import TextChunker, CustomChunker
from src.vector_store import VectorStoreManager
from src.llm_groq import GroqLLM
from src.config import get_config


def example_custom_chunking():
    """Example: Custom chunking strategies"""
    print("\n" + "="*60)
    print("EXAMPLE: Custom Chunking Strategies")
    print("="*60)
    
    # Load documents
    processor = DocumentProcessor()
    docs = processor.load_documents_from_directory()
    
    if not docs:
        print("No documents found")
        return
    
    # Standard chunking
    print("\n1. Standard Chunking (Recursive):")
    standard_chunker = TextChunker(chunk_size=500, chunk_overlap=100)
    standard_chunks = standard_chunker.chunk_documents(docs)
    print(f"   Created {len(standard_chunks)} chunks")
    
    # Paragraph-based chunking
    print("\n2. Paragraph-based Chunking:")
    para_chunks = CustomChunker.chunk_by_paragraph(docs, max_chars=500)
    print(f"   Created {len(para_chunks)} chunks")
    
    # Sentence-based chunking
    print("\n3. Sentence-based Chunking:")
    sent_chunks = CustomChunker.chunk_by_sentences(docs, max_sentences=5)
    print(f"   Created {len(sent_chunks)} chunks")


def example_vector_store_operations():
    """Example: Vector store operations"""
    print("\n" + "="*60)
    print("EXAMPLE: Vector Store Operations")
    print("="*60)
    
    config = get_config()
    store = VectorStoreManager()
    
    # Get stats
    print("\nVector Store Statistics:")
    stats = store.get_collection_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Search with threshold
    print("\nSearching with similarity threshold:")
    results = store.search_with_threshold(
        query="What is this about?",
        k=5,
        threshold=0.5
    )
    print(f"  Found {len(results)} results above threshold")


def example_llm_customization():
    """Example: LLM customization"""
    print("\n" + "="*60)
    print("EXAMPLE: LLM Customization")
    print("="*60)
    
    config = get_config()
    llm = GroqLLM(
        api_key=config.GROQ_API_KEY,
        temperature=0.3  # Lower temperature for factual answers
    )
    
    # Custom system prompt
    system_prompt = """You are an expert analyst. 
Provide detailed, structured answers.
Use bullet points where appropriate."""
    
    context = "Sample context about the topic"
    question = "Analyze this topic"
    
    answer = llm.generate_response_with_context(
        prompt=question,
        context=context,
        system_prompt=system_prompt
    )
    
    print(f"\nAnswer with custom system prompt:")
    print(answer)


def example_batch_processing():
    """Example: Process multiple documents"""
    print("\n" + "="*60)
    print("EXAMPLE: Batch Processing")
    print("="*60)
    
    config = get_config()
    processor = DocumentProcessor()
    chunker = TextChunker()
    store = VectorStoreManager()
    
    # Load all documents
    print("\n1. Loading all documents...")
    all_docs = processor.load_documents_from_directory()
    
    if not all_docs:
        print("No documents found")
        return
    
    # Chunk all documents
    print("\n2. Chunking all documents...")
    all_chunks = chunker.chunk_documents(all_docs)
    
    # Add to store in batches
    print("\n3. Adding to vector store...")
    store.add_documents(all_chunks, batch_size=50)
    
    print("✓ Batch processing complete")


def example_monitoring():
    """Example: Monitor system performance"""
    print("\n" + "="*60)
    print("EXAMPLE: System Monitoring")
    print("="*60)
    
    from src.rag_pipeline import RAGPipeline
    config = get_config()
    
    pipeline = RAGPipeline(groq_api_key=config.GROQ_API_KEY)
    pipeline.load_documents()
    pipeline.process_documents()
    
    # Get comprehensive stats
    stats = pipeline.get_pipeline_stats()
    
    print("\nPipeline Statistics:")
    print(f"  Documents: {stats['documents_loaded']}")
    print(f"  Chunks: {stats['chunks_created']}")
    print(f"  LLM Model: {stats['llm_model']}")
    
    print("\nChunking Stats:")
    chunk_stats = stats['chunking_stats']
    for key, value in chunk_stats.items():
        print(f"  {key}: {value}")
    
    print("\nVector Store Stats:")
    store_stats = stats['vector_store_stats']
    for key, value in store_stats.items():
        print(f"  {key}: {value}")


def main():
    """Run advanced examples"""
    print("\n" + "="*60)
    print("RAG SYSTEM - ADVANCED EXAMPLES")
    print("="*60)
    print("\nChoose an example:")
    print("1. Custom Chunking Strategies")
    print("2. Vector Store Operations")
    print("3. LLM Customization")
    print("4. Batch Processing")
    print("5. System Monitoring")
    print("0. Exit")
    
    choice = input("\nEnter choice: ").strip()
    
    try:
        if choice == "1":
            example_custom_chunking()
        elif choice == "2":
            example_vector_store_operations()
        elif choice == "3":
            example_llm_customization()
        elif choice == "4":
            example_batch_processing()
        elif choice == "5":
            example_monitoring()
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
