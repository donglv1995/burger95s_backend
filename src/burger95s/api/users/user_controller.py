from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_all_users():
    return [
        
    ]

@router.get("/users/{userid}")
async def get_user(userid: int):
    return {"username": "Dong", "age": 27}