from typing import Union


class ItemInfoDTO():
    def __init__(self, item_id: int, item_name: str, price: float, type: str, size: Union[str, None]=None, is_deleted: bool= False) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.type = type
        self.size = size
        self.is_deleted = is_deleted