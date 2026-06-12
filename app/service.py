from app.rag_pipeline import build_index
from app.qa import ask_question

store = build_index("data/pdfs")

def query_documents(question: str):
    return ask_question(store, question)