from app.embeddings import get_embedding
from vertexai.generative_models import GenerativeModel


def ask_question(store, question):

    # 1. question → vector
    q_embedding = get_embedding(question)

    # 2. retrieve relevant chunks
    results = store.search(q_embedding, top_k=5)

    context = ""
    sources = []

    for r in results:
        context += r["text"] + "\n\n"
        sources.append(r["source"])

    # 3. LLM call
    model = GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a precise assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

After answering, list sources used.

Format:
Answer: ...
Sources: {list(set(sources))}
"""

    response = model.generate_content(prompt)

    return response.text