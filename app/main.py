from fastapi import FastAPI

from app.models import QueryRequest
from app.service import query_documents

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/query")
def query(request: QueryRequest):

    answer = query_documents(request.question)

    return {
        "answer": answer
    }