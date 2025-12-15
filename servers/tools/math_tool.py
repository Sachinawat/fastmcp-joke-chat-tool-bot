import re
from servers.mcp_app import mcp

@mcp.tool
def solve_math(expression: str) -> str:
    """
    Solves basic math expressions safely.
    Supported: + - * / ( )
    """
    try:
        # Allow only safe characters
        if not re.match(r"^[0-9+\-*/().\s]+$", expression):
            return "❌ Invalid math expression"

        result = eval(expression, {"__builtins__": {}})
        return f"Result: {result}"

    except Exception as e:
        return f"❌ Math Error: {e}"
