# Test file for MCP server connection
import requests

def test_mcp_server():
    url = "http://localhost:4333/"
    try:
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_mcp_server()
