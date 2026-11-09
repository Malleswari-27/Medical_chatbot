
from dotenv import load_dotenv
import os

from src.helper import (
    load_pdf_file,
    filter_to_minimal_docs,
    text_split,
    download_hugging_face_embeddings,
)
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing from .env")

print("Step 1: Loading medical PDF...", flush=True)
extracted_data = load_pdf_file(data="data/")
print(f"PDF loading complete. Documents: {len(extracted_data)}", flush=True)

print("Step 2: Filtering documents...", flush=True)
filter_data = filter_to_minimal_docs(extracted_data)
print(f"Filtering complete. Documents: {len(filter_data)}", flush=True)

print("Step 3: Splitting text into chunks...", flush=True)
text_chunks = text_split(filter_data)
print(f"Chunking complete. Total chunks: {len(text_chunks)}", flush=True)

print("Step 4: Loading embedding model...", flush=True)
embeddings = download_hugging_face_embeddings()
print("Embedding model loaded successfully.", flush=True)

print("Step 5: Connecting to Pinecone...", flush=True)
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    print("Creating Pinecone index...", flush=True)
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

print("Step 6: Uploading document chunks to Pinecone...", flush=True)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("SUCCESS: Document chunks uploaded to Pinecone.", flush=True)
