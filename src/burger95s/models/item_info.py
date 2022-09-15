from pydantic import BaseModel, Field
from typing import Union


class ItemInfo(BaseModel):
    item_name: str
    price: float = Field(gt=0, title="The price must be greater than 0")
    type: str
    size: Union[str, None]=None
    is_deleted: bool = False

