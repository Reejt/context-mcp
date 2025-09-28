# Handles query answering from documents and general model

from fastmcp import FastMCP
from .document_ingestion import documents
from .model_manager import query_model
import os

mcp = FastMCP("My MCP Server")

def answer_query_raw(query: str) -> str:
    # Search in ingested documents stored in document_storage
    from os import listdir
    from os.path import isfile, join, abspath, dirname
    storage_dir = abspath(join(dirname(__file__), 'document_storage'))
    if not os.path.exists(storage_dir):
        return query_model(query)
    for filename in listdir(storage_dir):
        file_path = join(storage_dir, filename)
        if isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if query.lower() in content.lower():
                    return f"Found in document '{filename}': {content}"
            except Exception:
                continue
    # Fallback to model
    return query_model(query)

answer_query = mcp.tool(answer_query_raw)
