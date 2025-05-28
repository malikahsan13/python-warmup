import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import pickle

VECTOR_DB_PATH = "vector_store/faiss_index"

os.makedirs(os.path.dirname(VECTOR_DB_PATH), exist_ok=True)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

def get_text_chunks(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.create_documents([text])

def save_to_vector_store(text: str):
    chunks = get_text_chunks(text)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    with open(f"{VECTOR_DB_PATH}.pkl", "wb") as f:
        pickle.dump(vectorstore, f)

def load_vector_store():
    if not os.path.exists(f"{VECTOR_DB_PATH}.pkl"):
        return None
    with open(f"{VECTOR_DB_PATH}.pkl", "rb") as f:
        return pickle.load(f)

def query_vector_store(query: str):
    vectorstore = load_vector_store()
    if not vectorstore:
        return "No documents indexed yet."
    result = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in result])
