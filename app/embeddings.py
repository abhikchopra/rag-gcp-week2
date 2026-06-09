import vertexai
from vertexai.language_models import TextEmbeddingModel

vertexai.init(
    project="project-d97e020a-4925-4faa-a6c",
    location="us-central1"
)

model = TextEmbeddingModel.from_pretrained("text-embedding-005")


def get_embedding(text: str):
    """
    Converts a single text string into a vector embedding.
    """
    return model.get_embeddings([text])[0].values


def get_embeddings(texts, batch_size=5):
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]

        # safety: truncate super long chunks
        batch = [t[:2000] for t in batch]

        response = model.get_embeddings(batch)
        all_embeddings.extend([r.values for r in response])

    return all_embeddings