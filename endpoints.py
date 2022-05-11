from fastapi import APIRouter, HTTPException

endpoints = APIRouter(prefix='/operation')

operations = []

@endpoints.get('/')
async def list():
    return {
        "success": True,
        "data": operations,
        "size": len(operations)
    }


@endpoints.post('/{vlr}')
async def insert(vlr:float):
    operations.append(vlr)
    return{
        "success": True,
        "data": vlr
    }


@endpoints.delete('/{vlr}')
async def delete(vlr:float):
    try:
        operations.remove(vlr)
    except ValueError:
        raise HTTPException(status_code=404, detail="Valor não encontrado")

    return{
        "success": True
    }
