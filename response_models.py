from typing import Any, Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    success: bool


class OperationListResponse(BaseResponse):
    data: Any
    size: int

class OperationInsertResponse(BaseResponse):
    data: Any
    message: str
