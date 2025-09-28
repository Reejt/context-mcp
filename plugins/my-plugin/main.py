from fastapi import FastAPI, UploadFile, File, Form
from fastmcp import FastMCP
from .document_ingestion import ingest_file
from .query_handler import answer_query  
from .model_manager import switch_model

app = FastAPI(title="FastMCP Document-Aware Query Assistant")
mcp = FastMCP("FastMCP Document-Aware Query Assistant")


@app.post("/ingest")
async def ingest_endpoint(file: UploadFile = File(...)):
    # You may need to adapt ingest_file to accept file-like objects
    content = await file.read()
    result = ingest_file(content, filename=file.filename)
    return {"result": result}

@app.post("/query")
async def query_endpoint(query: str = Form(...)):
    result = answer_query(query)
    return {"result": result}

@app.post("/switch-model")
async def switch_model_endpoint(model_name: str = Form(...)):
    result = switch_model(model_name)
    return {"result": result}


    
