from fastapi import APIRouter

router = APIRouter()

@router.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI!"}

@router.get("/api/action1")
def action1():
    return {"message": "You triggered Action 1!"}

@router.get("/api/action2")
def action2():
    return {"message": "You triggered Action 2!"}
