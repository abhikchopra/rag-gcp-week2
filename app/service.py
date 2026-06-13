from app.storage import download_pdfs
from app.rag_pipeline import build_index
from app.qa import ask_question

pdf_folder = download_pdfs(
    "rag-week2-docs-abhik"
)

store = build_index(pdf_folder)

def query_documents(question: str):
    return ask_question(store, question)