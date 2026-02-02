from fastapi import FastAPI, HTTPException

from app.schemas import ToolResponse, ToolCall
from app.tools import Tools

app = FastAPI(title="MCP Server")

tools = Tools()

tool_registry = {
    "search_docs": tools.search_docs,
    "get_doc": tools.get_doc,
    "answer_with_context": tools.answer_with_context,
}

@app.post("/tools/call", response_model=ToolResponse)
def call_tool(request: ToolCall):
    tool = tool_registry.get(request.name)

    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    print(request.arguments['query'])
    result = tool(request.arguments['query'])

    return ToolResponse(result=result)