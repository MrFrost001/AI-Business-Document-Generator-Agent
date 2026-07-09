from pydantic import BaseModel

class RequestBody(BaseModel):
    request: str