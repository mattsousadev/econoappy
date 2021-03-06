from fastapi import APIRouter, HTTPException, Response

from app.models.request_models import InsertModel
from app.models.response_models import *

endpoints = APIRouter(prefix='/operation')

operations = []

@endpoints.get('/', response_model=OperationListResponse)
async def list():
    return OperationListResponse(
        success=True
        , data=operations
        , size=len(operations)
    )


@endpoints.post('/', response_model=OperationInsertResponse, status_code=201)
async def insert(insert_body:InsertModel):
    operations.append(insert_body)
    return OperationInsertResponse(
            success=True
            , data=insert_body
            , message="Registro inserido com sucesso!"
    )


@endpoints.delete('/{code}', status_code=204)
async def delete(code:str):
    try:
        to_delete = None
        for operation in operations:
            if operation.code == code:
                to_delete = operation
        
        if to_delete is None:
            raise ValueError
        else:
            operations.remove(to_delete)
    except ValueError:
        raise HTTPException(status_code=404, detail="Valor não encontrado")
    return Response(status_code=204)
