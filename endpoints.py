from fastapi import APIRouter, HTTPException

from request_models import InsertModel

endpoints = APIRouter(prefix='/operation')

operations = []

@endpoints.get('/')
async def list():
    return {
        "success": True,
        "data": operations,
        "size": len(operations)
    }


@endpoints.post('/')
async def insert(insert_body:InsertModel):
    operations.append(insert_body)
    return{
        "success": True,
        "data": insert_body
    }


@endpoints.delete('/{code}')
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

    return{
        "success": True
    }
