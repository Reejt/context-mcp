# Test file for MCP server HTTP POST
import requests

def test_mcp_ingest():
    url = "http://localhost:8000/ingest"
    files = {'file': ('test.txt', b'This is a test document.')}
    try:
        response = requests.post(url, files=files)
        print(f"/ingest Status code: {response.status_code}")
        print(f"/ingest Response: {response.text}")
    except Exception as e:
        print(f"/ingest POST failed: {e}")

def test_mcp_query():
    url = "http://localhost:8000/query"
    data = {'query': 'test'}
    try:
        response = requests.post(url, data=data)
        print(f"/query Status code: {response.status_code}")
        print(f"/query Response: {response.text}")
    except Exception as e:
        print(f"/query POST failed: {e}")

if __name__ == "__main__":
    test_mcp_ingest()
    test_mcp_query()
