from fastapi import APIRouter
from src.dummy_database import User, read_all_users, create_user, update_user,read_user_byId
import json

router = APIRouter()


@router.get("/users")
async def get_all_users():
    return read_all_users()


@router.get("/users/{userid}")
async def read_user(userid: int):
    return read_user_byId(userid=userid)


@router.post("/users")
async def create_new_user(u: User):
    return create_user(u)


@router.put("/users")
async def update_user_byid(userid: int, username: str, age: int):
    update_user(userid=userid, username=username, age=age)
    return 0
