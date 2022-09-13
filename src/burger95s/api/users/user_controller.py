from typing import List
from fastapi import APIRouter, status
import src.services.user_service as user_service
from ...models.user_info import User 

router = APIRouter(prefix='/users', tags=['users'])


@router.get("/", summary="Get all Users", response_model=List[User])
async def get_all_users():
    return user_service.get_all_users()


@router.get("/{userid}", summary="Get an User by ID", response_model=User)
async def get_user_by_ID(userid):
    return user_service.get_user_by_id(userid=userid)


@router.post("/", summary="Create an User")
async def create_user(user: User):
    return user_service.create_user(user=user)
    


@router.put("/{userid}", summary="Update Information's User")
async def update_user_by_id(user: User):
    return user_service.update_user(user=user)


@router.put("/", summary="Delete an User by ID")
async def delete_user_by_ID(userid, is_hard_delete: bool=False):
    return user_service.delete_user(userid=userid, is_hard_delete=is_hard_delete)
