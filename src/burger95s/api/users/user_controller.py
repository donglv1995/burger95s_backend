from typing import List
from fastapi import APIRouter, Body, Form, status
import src.services.user_service as user_service
from src.burger95s.models.user_info import UserInfo
# from src.burger95s.dto.user_info_dto import UserInfoDTO

router = APIRouter(prefix='/users', tags=['users'])


@router.get("/", summary="Get all Users")
async def get_all_users():
    return user_service.get_all_users()


@router.get("/{user_id}", summary="Get an User by ID")
async def get_user_by_ID(user_id):
    return user_service.get_user_by_id(user_id=user_id)


@router.post("/", summary="Create an User", status_code= status.HTTP_201_CREATED)
async def create_user(user: UserInfo = Body(
    example={
        "user_name": "Quan",
        "gender": "Male",
        "phone": "01882587321"
    })):
    return user_service.create_user(user=user)
    


@router.put("/{user_id}", summary="Update Information's User", status_code= status.HTTP_202_ACCEPTED)
async def update_user_by_id(user_id, user: UserInfo= Body(
    example={
        "user_name": "Lily",
        "gender": "Female",
        "phone": "0123-025-789"
    })):
    return user_service.update_user(user_id=user_id, user=user)


@router.put("/{user_id}/{delete}", summary="Delete User by ID", status_code=status.HTTP_202_ACCEPTED)
async def delete_user_by_ID(user_id, is_hard_delete: bool=False):
    return user_service.delete_user(user_id=user_id, is_hard_delete=is_hard_delete)
