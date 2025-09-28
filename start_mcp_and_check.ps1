# PowerShell script to start MCP server and check Gemini connection
# Save as start_mcp_and_check.ps1 and run in your workspace

Write-Host "Starting MCP server on port 4333..."
Start-Process -NoNewWindow -FilePath "node" -ArgumentList "./node_modules/mcp-server/bin/server.js --port 4333"

Start-Sleep -Seconds 3

Write-Host "Checking Gemini MCP connection..."
gemini mcp list

Write-Host "If 'Connected' does not appear, check MCP server logs and port usage."
