from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Tripathi"}

@app.get("/items/{itemid}")
async def read_items(itemid: int):
    return {"itemid": itemid} 