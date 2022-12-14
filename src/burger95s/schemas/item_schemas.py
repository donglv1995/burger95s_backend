from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    quantity: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase): # schema builds for Item
    id: int

    class Config:
        orm_mode = True


class DeletedItem(Item):
    out_of_stock: bool




class ItemBurger(BaseModel): # working with Burger model
    item_id: int
    quantity: int

    class Config:
        orm_mode = True