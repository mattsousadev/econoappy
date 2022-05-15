from pydantic import BaseModel

class InsertModel(BaseModel):
    code: str
    value: float
    description: str