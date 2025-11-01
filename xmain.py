from fastapi import FastAPI

app = FastAPI() 

@app.get('/')
async def root():
    return "Hello ji!"

@app.get("/items/{itemid}")
async def items(itemid: int):
    return f"itemid: {itemid}"