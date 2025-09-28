from fastapi import FastAPI, UploadFile, File, Form
from fastmcp import FastMCP
from .document_ingestion import ingest_file_raw
from .query_handler import answer_query_raw
from .model_manager import switch_model
import os

app = FastAPI(title="FastMCP Document-Aware Query Assistant")
mcp = FastMCP("FastMCP Document-Aware Query Assistant")


@app.post("/ingest")
async def ingest_endpoint(file: UploadFile = File(...)):
    # Save uploaded file to document_storage and pass its path to ingest_file_raw
    storage_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'document_storage'))
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    file_path = os.path.join(storage_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = ingest_file_raw(file_path)
    return {"result": result}

@app.post("/query")
async def query_endpoint(query: str = Form(...)):
    result = answer_query_raw(query)
    return {"result": result}

@app.post("/switch-model")
async def switch_model_endpoint(model_name: str = Form(...)):
    result = switch_model(model_name)
    return {"result": result}


    
