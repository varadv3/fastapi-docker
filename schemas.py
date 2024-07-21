from pydantic import BaseModel

class Code(BaseModel):
    source_code: str
    input: str = None