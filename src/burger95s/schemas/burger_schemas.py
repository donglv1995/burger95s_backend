from typing import List, Union

from pydantic import BaseModel

from .item_schemas import ItemBurger

from src.burger95s import constant


class BurgerBase(BaseModel):
    name: Union[str, None] = None
    type: Union[str, None] = None




class Burger(BurgerBase):
    id: int # If id = -1, burger is custome type
    items: List[ItemBurger] # only receive item_id and quantity
    
    class Config:
        orm_mode = True



class BurgerUpdated(Burger):
    is_deleted: str
