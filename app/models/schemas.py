from pydantic import BaseModel

class ExplainRequest(BaseModel):
    topic: str
    language: str
 
class ExplainResponse(BaseModel):
    original: str
    translated: str
    language: str 