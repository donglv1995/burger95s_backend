from pydantic import BaseModel


class UserInfo(BaseModel):
    user_name: str
    gender: str
    phone: str
    is_deleted: str= False


class Users(UserInfo):
    user_id: int






