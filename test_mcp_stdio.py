# Test file for MCP stdio connection
import subprocess

def test_mcp_stdio():
    try:
        proc = subprocess.Popen([
            "node", "./node_modules/mcp-server/bin/server.js", "--port", "4333"
        ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Send a simple command if MCP server supports stdio commands
        proc.stdin.write("ping\n")
        proc.stdin.flush()
        output = proc.stdout.readline()
        print(f"STDIO response: {output}")
        proc.terminate()
    except Exception as e:
        print(f"STDIO connection failed: {e}")

if __name__ == "__main__":
    test_mcp_stdio()
