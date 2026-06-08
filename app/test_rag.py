from rag_pipeline import build_index

store = build_index("data/sample.pdf")

print("RAG pipeline built successfully")