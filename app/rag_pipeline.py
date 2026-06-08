import os
from utils import extract_text, chunk_text
from embeddings import get_embeddings
from vector_store import VectorStore


def build_index(folder_path):
    all_chunks = []
    all_embeddings = []
    metadata = []

    # STEP 1: loop over PDFs
    for file in os.listdir(folder_path):
        if not file.endswith(".pdf"):
            continue

        pdf_path = os.path.join(folder_path, file)

        # STEP 2: extract text
        text = extract_text(pdf_path)

        # STEP 3: chunk
        chunks = chunk_text(text)

        # STEP 4: embeddings
        embeddings = get_embeddings(chunks)

        # STEP 5: store with metadata
        all_chunks.extend(chunks)
        all_embeddings.extend(embeddings)
        metadata.extend([file] * len(chunks))

    # STEP 6: store in FAISS
    store = VectorStore(dimension=768)
    store.add(all_embeddings, all_chunks, metadata)

    return store