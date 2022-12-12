from src.database.repositories.item_repository import ItemRepository
from src.burger95s.schemas import item_schemas

class ItemService:
    def __init__(self, item_repository: ItemRepository) -> None:
        self.item_repository: ItemRepository = item_repository
        
    
    def get_items(self):
        return self.item_repository.get_items()

    
    def get_item_by_id(self, item_id: int):
        return self.item_repository.get_item_by_id(item_id=item_id)
        
    
    def create_item(self, item: item_schemas.ItemCreate):
        return self.item_repository.create_item(item=item)

    
    def soft_delete_item_by_id(self, item_id: int):
        return  self.item_repository.soft_delete_item_by_id(item_id=item_id)
        