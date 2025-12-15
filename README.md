# fastmcp-joke-chat-tool-bot

An example project demonstrating a simple Multi-Context Protocol (MCP) server and client using FastMCP, with two tools: a chatbot and a joke explainer.

## Features

- **Chat Tool**: General-purpose AI chatbot using OpenAI's API.
- **Joke Tool**: Explains jokes or cracks new ones using OpenAI's API.
- **MCP Server**: Unified server exposing both tools via HTTP.
- **Async Client**: Command-line client to interact with the server and select tools automatically.

## Project Structure

- `servers/server.py`: Starts the MCP server and registers tools.
- `servers/mcp_app.py`: Initializes the FastMCP app instance.
- `servers/tools/chat_tool.py`: Implements the chat tool.
- `servers/tools/joke_tool.py`: Implements the joke tool.
- `clients/client.py`: Async CLI client for interacting with the server.
- `requirements.txt`: Python dependencies.

## Setup

1. **Clone the repository**
2. **Install dependencies**:
	```bash
	pip install -r requirements.txt
	```
3. **Set environment variables**:
	- Create a `.env` file with your OpenAI API key:
	  ```env
	  OPENAI_API_KEY=your_openai_api_key
	  OPENAI_MODEL=gpt-4o-mini
	  ```

## Running the Server

```bash
python servers/server.py
```
The server will start on `http://127.0.0.1:8000/mcp`.

## Using the Client

```bash
python clients/client.py
```
Type your message. If it contains the word "joke", the joke tool is used; otherwise, the chat tool is used. Type `exit` to quit.

## Example

```
You: Tell me a joke about computers.
[explain_joke] → (AI-generated joke or explanation)

You: How do I reverse a list in Python?
[chat] → (AI-generated answer)
```

## Credits

- Built with [FastMCP](https://github.com/ericmjl/fastmcp) and [OpenAI API](https://platform.openai.com/docs/api-reference/introduction).

---
MIT License