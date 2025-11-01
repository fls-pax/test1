from fastapi import APIRouter, status

router = APIRouter()

@router.get("/hello/{name}", status_code=status.HTTP_200_OK)
def hello(name: str, excited: bool = False) -> dict:
    msg = f"hello, {name} {'!!!' if excited else ''}"
    return {"msg": msg}



