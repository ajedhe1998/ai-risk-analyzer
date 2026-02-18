# Release Risk Analyzer (Sample AI App)

A minimal, deployable sample app that demonstrates:

- LangChain
- RAG (Retrieval Augmented Generation)
- MCP-style connectors (simulated)
- Open-source LLM via Ollama
- FastAPI backend
- Dockerized deployment

## What it does

The app ingests release-related signals (test failures, deployment history, commit notes), stores them in a vector database, and uses an LLM to analyze release risk.

## Quick Start

### 1) Prerequisites

- Python 3.11+
- Docker (optional but recommended)
- Ollama installed locally

Install a model:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the app

```bash
uvicorn app.main:app --reload
```

Open:

http://localhost:8000/docs

### 4) Test endpoint

```bash
curl "http://localhost:8000/analyze"
```

## Project Structure

```
release-risk-analyzer/
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── risk_agent.py
│   └── mcp_connectors/
│       ├── git_connector.py
│       ├── jenkins_connector.py
│       └── test_report_connector.py
├── data/
│   ├── deployment_history.txt
│   ├── release_notes.txt
│   └── failed_tests.json
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```
