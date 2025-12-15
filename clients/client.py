import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

# def select_tool(user_input: str) -> tuple[str, dict]:
#     """
#     Simple router logic.
#     Later you can replace this with an LLM router.
#     """
#     if "joke" in user_input.lower():
#         return "explain_joke", {"joke": user_input}
#     else:
#         return "chat", {"prompt": user_input}

def select_tool(user_input: str) -> tuple[str, dict]:
    text = user_input.lower()

    if "joke" in text:
        return "explain_joke", {"joke": user_input}

    if "summarize" in text or "summary" in text:
        return "summarize", {"text": user_input}

    if any(x in text for x in ["+", "-", "*", "/", "calculate", "solve"]):
        return "solve_math", {"expression": user_input}

    return "chat", {"prompt": user_input}


async def main():
    async with client:
        print("\n🤖 MCP Assistant (type 'exit' to quit)\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ("exit", "quit"):
                break

            tool_name, payload = select_tool(user_input)
            result = await client.call_tool(tool_name, payload)

            print(f"\n[{tool_name}] → {result.data}\n")

if __name__ == "__main__":
    asyncio.run(main())
