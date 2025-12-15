# Start MCP server
from servers.mcp_app import mcp

# Import tools so they register
from servers.tools import chat_tool, joke_tool, summary_tool, math_tool 

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
