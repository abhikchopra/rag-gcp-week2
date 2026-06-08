from embeddings import get_embedding
from vertexai.generative_models import GenerativeModel

MODEL = GenerativeModel("gemini-2.5-flash")


def ask_question(store, question):

    q_embedding = get_embedding(question)

    results = store.search(q_embedding, top_k=5)

    context = "\n\n".join(
        [f"[Source: {r['source']}]\n{r['text']}" for r in results]
    )

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

If not found, say "Not found in documents".
"""

    response = MODEL.generate_content(prompt)
    return response.text