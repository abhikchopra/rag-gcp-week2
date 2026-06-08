import vertexai
from vertexai.language_models import TextEmbeddingModel

PROJECT_ID = "project-d97e020a-4925-4faa-a6c"
REGION = "us-central1"

vertexai.init(project=PROJECT_ID, location=REGION)

# Load model once (important optimization)
model = TextEmbeddingModel.from_pretrained("text-embedding-005")


def get_embedding(text: str):
    """
    Single text embedding (use for testing or queries)
    """
    return model.get_embeddings([text])[0].values


def get_embeddings(texts: list[str]):
    """
    Batch embeddings (use for RAG ingestion - FAST + scalable)
    """
    response = model.get_embeddings(texts)
    return [r.values for r in response]