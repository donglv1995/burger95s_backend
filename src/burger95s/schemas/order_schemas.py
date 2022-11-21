import datetime
from typing import List

from pydantic import BaseModel

from src.burger95s.schemas import burger_schemas


class OrderBase(BaseModel):
    consumer_name: str
    ordered_date: datetime.datetime = None
    ordering: List[burger_schemas.Burger]


class OrderCreate(OrderBase):
    pass



class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True



class OrderDeleted(Order):
    is_deleted: str
