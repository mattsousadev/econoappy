import uvicorn
from fastapi import FastAPI

import endpoints

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello World'

app.include_router(endpoints.endpoints)

if __name__ == '__main__':
    uvicorn.run(app)