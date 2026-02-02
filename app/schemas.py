from pydantic import BaseModel
from typing import Any, Dict

class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]

class ToolResponse(BaseModel):
    result: Any

