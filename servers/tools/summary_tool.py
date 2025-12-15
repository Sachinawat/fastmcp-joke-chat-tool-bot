import os
from dotenv import load_dotenv
from openai import OpenAI
from servers.mcp_app import mcp

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

@mcp.tool
def summarize(text: str) -> str:
    """
    Summarizes the given text clearly and concisely.
    """
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You summarize text clearly and concisely."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ OpenAI Error: {e}"
