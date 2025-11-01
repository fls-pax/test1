from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello Tripathi"}

@app.get("/items/{itemid}")
async def read_items(itemid: int):
    return {"itemid": itemid} 


# test comment