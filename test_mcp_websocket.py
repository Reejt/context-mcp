# Test file for MCP server WebSocket (if supported)
import websocket

def test_mcp_websocket():
    url = "ws://localhost:4333/"
    try:
        ws = websocket.create_connection(url)
        ws.send("ping")
        result = ws.recv()
        print(f"WebSocket response: {result}")
        ws.close()
    except Exception as e:
        print(f"WebSocket connection failed: {e}")

if __name__ == "__main__":
    test_mcp_websocket()
