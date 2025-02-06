import sys
import os
import shutil  # For deleting existing vector store

# ✅ Ensure Python can find `scraper.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma  # ✅ Corrected Import
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ Updated Import
from scraper.scraper import scrape_brainlox  # Import the scraper function

def create_vector_store():
    print("🚀 Starting Vector Store Creation...")

    # ✅ Check if `chroma_db` exists and remove if necessary
    db_path = os.path.abspath("./chroma_db")  # Use absolute path
    if os.path.exists(db_path):
        if os.path.isdir(db_path):
            print("⚠️ Removing existing ChromaDB directory...")
            shutil.rmtree(db_path)
        else:
            print("⚠️ Deleting existing chroma_db file...")
            os.remove(db_path)

    # ✅ Step 1: Scrape course data
    text_data = scrape_brainlox()
    if not text_data:
        print("❌ No data scraped! Check if the website structure has changed.")
        return None

    print("✅ Scraped Data Successfully!")

    # ✅ Step 2: Split data into chunks for embeddings
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.create_documents([text_data])

    print(f"📄 Data split into {len(texts)} chunks for embedding.")

    # ✅ Step 3: Use Hugging Face for Embeddings (Free Alternative to OpenAI)
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    except Exception as e:
        print(f"❌ Error initializing embeddings: {e}")
        return None

    print("✅ Hugging Face Embeddings initialized successfully.")

    # ✅ Step 4: Store in ChromaDB
    try:
        vector_db = Chroma.from_documents(texts, embeddings, persist_directory=db_path)
        print("✅ Vector store created and persisted at:", db_path)
    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        return None

    return vector_db

if __name__ == "__main__":
    create_vector_store()