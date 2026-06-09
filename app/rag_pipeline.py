import os
from app.utils import extract_text, chunk_text
from app.embeddings import get_embeddings
from app.vector_store import VectorStore


def build_index(folder_path):

    store = VectorStore(dimension=768)

    # 🔥 cost controls
    MAX_FILES = 10
    MAX_CHUNKS_PER_FILE = 200
    MAX_TOTAL_CHUNKS = 1000

    all_chunks = []
    all_embeddings = []
    all_sources = []

    for idx, file in enumerate(os.listdir(folder_path)):

        if idx >= MAX_FILES:
            break

        if file.endswith(".pdf"):

            file_path = os.path.join(folder_path, file)

            text = extract_text(file_path)
            chunks = chunk_text(text)

            # 🔥 limit per document
            chunks = chunks[:MAX_CHUNKS_PER_FILE]

            # stop global explosion
            if len(all_chunks) > MAX_TOTAL_CHUNKS:
                break

            embeddings = get_embeddings(chunks)

            all_chunks.extend(chunks)
            all_embeddings.extend(embeddings)
            all_sources.extend([file] * len(chunks))

    store.add(all_embeddings, all_chunks, all_sources)

    return store
    print(f"Processing file: {file}")
    print(f"Chunks: {len(chunks)}")