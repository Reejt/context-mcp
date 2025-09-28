# Handles query answering from documents and general model

from fastmcp import FastMCP
from .document_ingestion import documents
from .model_manager import query_model

mcp = FastMCP("My MCP Server")

@mcp.tool
def answer_query(query: str) -> str:
    # Simple keyword search in ingested documents
    for doc in documents:
        if query.lower() in doc.lower():
            return f"Found in document: {doc}"
    # Fallback to model
    return query_model(query)
