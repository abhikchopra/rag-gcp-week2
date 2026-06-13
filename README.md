# RAG on Google Cloud Platform

Production-oriented Retrieval Augmented Generation (RAG) system built using:

* FastAPI
* Docker
* Google Cloud Run
* Vertex AI Gemini
* Vertex AI Embeddings
* Cloud Storage
* IAM
* GitHub Actions (CI/CD)

---

## Architecture

User
↓
FastAPI
↓
Cloud Run
↓
IAM
↓
Cloud Storage
↓
Vertex AI Embeddings
↓
FAISS
↓
Gemini
↓
Answer

---

## Features

* PDF ingestion
* Document chunking
* Embedding generation
* Semantic retrieval
* Generative answering
* Cloud-native deployment
* IAM secured endpoints
* Logging & observability
* Versioned deployments
* Rollback support

---

## Tech Stack

| Layer      | Technology         |
| ---------- | ------------------ |
| API        | FastAPI            |
| Container  | Docker             |
| Deployment | Cloud Run          |
| Storage    | Cloud Storage      |
| Embeddings | text-embedding-005 |
| LLM        | Gemini             |
| Retrieval  | FAISS              |
| Security   | IAM                |
| CI/CD      | GitHub Actions     |

---

## Deployment

```bash
docker buildx build \
--platform linux/amd64 \
-t IMAGE \
--push .
```

```bash
gcloud run deploy ...
```

---

## Learning Objectives

This project explores:

* Cloud-native AI architectures
* Retrieval Augmented Generation
* Vertex AI
* Cloud Run
* IAM
* DevOps
* CI/CD
* Production operations
