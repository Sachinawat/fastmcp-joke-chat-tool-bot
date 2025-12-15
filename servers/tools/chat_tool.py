import os
from dotenv import load_dotenv
from openai import OpenAI
from servers.mcp_app import mcp

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

conversation = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

@mcp.tool
def chat(prompt: str) -> str:
    """General purpose chatbot"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation + [{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "user", "content": prompt})
    conversation.append({"role": "assistant", "content": reply})
    return reply
