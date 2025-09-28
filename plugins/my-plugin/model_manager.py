# Handles model switching and querying
from fastmcp import FastMCP

current_model = "gemini"

mcp = FastMCP("My MCP Server")

@mcp.tool
def switch_model(model_name: str) -> str:
    global current_model
    current_model = model_name
    return f"Model switched to {model_name}"

def query_model(query: str) -> str:
    # Placeholder: Integrate with Gemini CLI or other models
    # Use current_model to select backend
    return f"General answer from {current_model}: [model response here]"
