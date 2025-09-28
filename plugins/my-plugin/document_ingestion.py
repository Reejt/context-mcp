# Handles document ingestion and parsing
from fastmcp import FastMCP

import os
import shutil

def extract_text_from_file(file_path: str) -> str:
    """Extracts text from a plain text file. Extend for other formats as needed."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
documents = []

mcp = FastMCP("My MCP Server")

def ingest_file_raw(file_path: str) -> str:
    try:
        storage_dir = os.path.join(os.path.dirname(__file__), 'document_storage')
        storage_dir = os.path.abspath(storage_dir)
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        filename = os.path.basename(file_path)
        dest_path = os.path.join(storage_dir, filename)
        shutil.copy2(file_path, dest_path)
        content = extract_text_from_file(dest_path)
        documents.append(content)
        return f"File '{file_path}' ingested and stored at '{dest_path}'."
    except Exception as e:
        return f"Error ingesting file: {str(e)}"

ingest_file = mcp.tool(ingest_file_raw)
