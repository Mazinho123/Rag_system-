"""
Main Application Module
Interactive RAG system interface
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import get_config
from src.rag_pipeline import RAGPipeline


class RAGApplication:
    """Interactive RAG Application"""
    
    def __init__(self):
        """Initialize application"""
        try:
            self.config = get_config()
            self.pipeline = RAGPipeline(
                groq_api_key=self.config.GROQ_API_KEY,
                vector_store_path=self.config.VECTOR_STORE_PATH,
                documents_path=self.config.DOCUMENTS_PATH,
                chunk_size=self.config.CHUNK_SIZE,
                chunk_overlap=self.config.CHUNK_OVERLAP
            )
        except Exception as e:
            print(f"✗ Error initializing application: {str(e)}")
            raise
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("RAG SYSTEM - INTERACTIVE MENU")
        print("="*60)
        print("1. Load documents from directory")
        print("2. Load single document")
        print("3. Process documents (chunk and embed)")
        print("4. Ask a question")
        print("5. Ask multiple questions")
        print("6. View statistics")
        print("7. Reset pipeline")
        print("8. View configuration")
        print("9. Exit")
        print("="*60)
    
    def load_documents_menu(self):
        """Handle document loading"""
        print("\n1. Load from directory (default: ./data)")
        print("2. Load specific file")
        choice = input("Choose option (1 or 2): ").strip()
        
        if choice == "1":
            directory = input("Enter directory path (press Enter for default ./data): ").strip()
            if not directory:
                directory = None
            count = self.pipeline.load_documents(directory=directory)
            print(f"✓ Loaded {count} documents")
        elif choice == "2":
            file_path = input("Enter file path: ").strip()
            if file_path:
                count = self.pipeline.load_documents(file_path=file_path)
                print(f"✓ Loaded {count} documents")
        else:
            print("✗ Invalid choice")
    
    def process_documents_menu(self):
        """Handle document processing"""
        if not self.pipeline.documents:
            print("✗ No documents loaded. Load documents first.")
            return
        
        chunk_count = self.pipeline.process_documents()
        print(f"✓ Created {chunk_count} chunks and embedded them")
    
    def ask_question_menu(self):
        """Handle single question"""
        question = input("\n❓ Enter your question: ").strip()
        if not question:
            return
        
        result = self.pipeline.query(question, k=self.config.K_RETRIEVED_DOCS)
        
        print("\n" + "="*60)
        print("ANSWER:")
        print("="*60)
        print(result["answer"])
        print("="*60)
        
        if result["sources"]:
            print("\nSOURCES:")
            for source in result["sources"]:
                print(f"\n[Document {source['document']}]")
                print(f"Content: {source['content']}")
                print(f"Metadata: {source['metadata']}")
    
    def ask_multiple_questions_menu(self):
        """Handle multiple questions"""
        questions = []
        print("\nEnter questions (one per line, empty line to finish):")
        while True:
            q = input("> ").strip()
            if not q:
                break
            questions.append(q)
        
        if not questions:
            print("No questions entered")
            return
        
        results = self.pipeline.batch_query(questions, k=self.config.K_RETRIEVED_DOCS)
        
        print("\n" + "="*60)
        print("BATCH RESULTS")
        print("="*60)
        for i, result in enumerate(results, 1):
            print(f"\n[{i}] Question: {result['question']}")
            print(f"Answer: {result['answer'][:200]}...")
    
    def view_statistics(self):
        """Display pipeline statistics"""
        self.pipeline.display_stats()
    
    def reset_pipeline(self):
        """Reset pipeline"""
        confirm = input("Are you sure you want to reset? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.pipeline.reset_pipeline()
            print("✓ Pipeline reset")
    
    def view_configuration(self):
        """Display configuration"""
        self.config.display()
    
    def run(self):
        """Run interactive application"""
        print("\n" + "="*60)
        print("WELCOME TO RAG SYSTEM")
        print("="*60)
        print("Retrieval Augmented Generation with Groq LLM")
        print("="*60)
        
        while True:
            self.display_menu()
            choice = input("Enter choice (1-9): ").strip()
            
            try:
                if choice == "1":
                    self.load_documents_menu()
                elif choice == "2":
                    self.load_documents_menu()
                elif choice == "3":
                    self.process_documents_menu()
                elif choice == "4":
                    self.ask_question_menu()
                elif choice == "5":
                    self.ask_multiple_questions_menu()
                elif choice == "6":
                    self.view_statistics()
                elif choice == "7":
                    self.reset_pipeline()
                elif choice == "8":
                    self.view_configuration()
                elif choice == "9":
                    print("\n👋 Goodbye!")
                    break
                else:
                    print("✗ Invalid choice. Please try again.")
            except KeyboardInterrupt:
                print("\n\n👋 Application interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"✗ Error: {str(e)}")


def main():
    """Main entry point"""
    try:
        app = RAGApplication()
        app.run()
    except Exception as e:
        print(f"✗ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
