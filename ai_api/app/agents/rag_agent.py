from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
import os, pickle

VECTOR_DB_PATH = "vector_store/faiss_index.pkl"

def load_vector_store():
    if not os.path.exists(VECTOR_DB_PATH):
        return None
    with open(VECTOR_DB_PATH, "rb") as f:
        return pickle.load(f)

def get_rag_response(query: str):
    vectorstore = load_vector_store()
    if not vectorstore:
        return "No knowledge base found."

    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.2)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
    )

    result = qa_chain.run(query)
    return result
