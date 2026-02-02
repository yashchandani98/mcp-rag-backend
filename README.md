# mcp-rag-backend
Setup instructions:
- run pip install -r requirements.txt in a virtual environment
- setup openrouter API key in .env with OPENROUTER_API_KEY name
- run uvicorn app.main:app --reload
- try hitting HTTP request: POST http://localhost:8000/tools/call with following request body:
{
  "name": "answer_with_context",
  "arguments": {
    "query": <ask your question here>
  }
}
