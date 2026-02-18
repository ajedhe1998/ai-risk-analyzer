from fastapi import FastAPI
from app.rag_pipeline import build_retriever
from app.risk_agent import create_risk_agent
from app.mcp_connectors.git_connector import load_git_context
from app.mcp_connectors.jenkins_connector import load_jenkins_context
from app.mcp_connectors.test_report_connector import load_test_context

app = FastAPI(title="Release Risk Analyzer")

# --- Simulated MCP connector outputs ---
docs = []
docs.extend(load_git_context())
docs.extend(load_jenkins_context())
docs.extend(load_test_context())

retriever = build_retriever(docs)
agent = create_risk_agent(retriever)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze")
def analyze():
    query = (
        "Analyze the release risk using the provided context. "
        "Return risk level (High/Medium/Low), key risks, and recommendations."
    )
    result = agent.invoke({"query": query})
    return {"analysis": result["result"]}
