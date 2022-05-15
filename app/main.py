import uvicorn
from fastapi import FastAPI

from app.api import endpoints

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello World'

app.include_router(endpoints.endpoints)

