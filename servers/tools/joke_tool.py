import os
from dotenv import load_dotenv
from openai import OpenAI
from servers.mcp_app import mcp

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

@mcp.tool
def explain_joke(joke: str) -> str:
    """Explains jokes only"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You crack new jokes."
            },
            {
                "role": "user",
                "content": joke
            }
        ]
    )
    return response.choices[0].message.content.strip()
