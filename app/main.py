from fastapi import FastAPI
import logging
import time

from app.models import QueryRequest
from app.service import query_documents

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/query")
def query(request: QueryRequest):

    start_time = time.time()

    logging.info("Request received")
    logging.info(f"Question length: {len(request.question)}")

    try:
        answer = query_documents(request.question)

        duration = round(time.time() - start_time, 2)

        logging.info("Response generated")
        logging.info(f"Duration: {duration} seconds")

        return {
            "answer": answer
        }

    except Exception:

        logging.exception("Query failed")

        raise