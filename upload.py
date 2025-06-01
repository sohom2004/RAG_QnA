import argparse
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def load_documents(path):
    loader = DirectoryLoader(path, glob="*.md")
    document = loader.load()
    return document

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len,
        is_separator_regex=True,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

def store_in_chroma(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory="./chroma"
    )
    vector_store.add_documents(chunks)
    print("Documents uploaded and persisted to ChromaDB.")

def main():
    parser = argparse.ArgumentParser(description="Upload the markdown document to ChromaDB.")
    parser.add_argument("path", type=str, help="Path to the resources directory containing markdown files.")
    args = parser.parse_args()
    
    documents = load_documents(args.path)
    chunks = split_documents(documents)
    
    store_in_chroma(chunks)
    print("Upload completed successfully.")
    
if __name__ == "__main__":
    main()