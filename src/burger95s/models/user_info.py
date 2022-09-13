from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    user_id: Union[int, None] = None
    user_name: str
    gender: str
    phone: Union[str, None] = None
    is_deleted: str

