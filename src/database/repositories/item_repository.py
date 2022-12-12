from sqlalchemy.orm import Session
from src.burger95s.models import models
from src.burger95s.schemas import item_schemas



class ItemRepository:
    def __init__(self, session_factory: Session) -> None:
        self.session_factory = session_factory
    
    def get_items(self):
        with self.session_factory() as session:
            return session.query(models.Item.id, models.Item.name, models.StorageItem.quantity)\
                            .join(models.StorageItem)\
                            .where(models.Item.id == models.StorageItem.item_id, models.StorageItem.out_of_stock == False).all()
    
    def get_item_by_id(self, item_id: int):
        with self.session_factory() as session:
            item =  session.query(models.Item.id, models.Item.name, models.StorageItem.quantity)\
                    .join(models.StorageItem)\
                    .where(
                        models.Item.id == item_id, 
                        models.Item.id == models.StorageItem.item_id, 
                        models.StorageItem.out_of_stock == False
                    ).first()

            if not item:
                raise ItemNotFound(item_id)

            return item
    
    def create_item(self, item: item_schemas.ItemCreate):
        with self.session_factory() as session:
            item_info = models.Item(item.name)
            session.add(item_info)  
            session.flush()

            item_storage = models.StorageItem(item_id=item_info.id, quantity=item.quantity)
            session.add(item_storage)

            session.commit()
            session.refresh(item_info)
            session.refresh(item_storage)

            return item_info
            


    def soft_delete_item_by_id(self, item_id):
        with self.session_factory() as session:
            session.query(models.StorageItem)\
                .filter(models.StorageItem.item_id == item_id)\
                .update(
                    {models.StorageItem.out_of_stock: True},
                    synchronize_session=False
                )
            session.flush()
            session.commit()

            item = session.query(models.Item.id, models.Item.name, models.StorageItem.quantity, models.StorageItem.out_of_stock)\
                    .join(models.StorageItem)\
                    .where(
                        models.Item.id == item_id, 
                        models.Item.id == models.StorageItem.item_id
                    ).first()

            if not item:
                raise ItemNotFound(item_id)

            return item

class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id) -> None:
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ItemNotFound(NotFoundError):
    entity_name: str = "Item"

