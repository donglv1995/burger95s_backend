# from sqlalchemy.orm import joinedload

from src.burger95s.schemas import item_schemas
from src.database import database
from src.burger95s.models import models

# default
def get_items(): # return available items in Storage include: ID, name, quantity
    with database.get_db() as db:
        return db.query(models.Item.id,models.Item.name,models.StorageItem.quantity)\
                    .join(models.StorageItem) \
                        .where(models.StorageItem.item_id == models.Item.id, \
                                models.StorageItem.out_of_stock == False).all()



def get_item_by_id(item_id: int):
    with database.get_db() as db:
        return db.query(models.Item.id,models.Item.name,models.StorageItem.quantity)\
                    .join(models.StorageItem) \
                    .where(models.StorageItem.item_id == item_id, \
                         models.StorageItem.out_of_stock == False).first()





def create_item(item: item_schemas.ItemCreate):
    with database.get_db() as db:
        # create item with id and name
        db_item = models.Item(name=item.name)
        db.add(db_item)
        db.commit() # commit first to get PK of new Item

        # create quantity and item_id for item in storage
        db_storage_item = models.StorageItem(quantity=item.quantity, item_id=db_item.id).first()
        db.add(db_storage_item)
        db.commit()
        

        return db_storage_item



def delete_item_storage_by_id(item_id: int): # soft delete
    with database.get_db() as db:
        try:
            deleted_item = db.query(models.StorageItem) \
                                .filter(models.StorageItem.item_id==item_id) \
                                .update(
                                        {models.StorageItem.out_of_stock: True},
                                        synchronize_session=False
                                    )

            db.commit()
            return deleted_item

        except:
            raise Exception('cannot delete the item, maybe there something wrong with the id or item does not exist')
        


def update_item_storage(item: item_schemas.Item): # adding quantity to Item
    with database.get_db() as db:
        try:
            db_item = db.query(models.StorageItem)\
                            .filter(models.StorageItem.item_id == item.id)\
                            .update(
                                {models.StorageItem.quantity: models.StorageItem.quantity + item.quantity},                   
                                synchronize_session=False
                            )

            db.commit()

            return db_item
            
        except :
            raise Exception("it's not working at the Repository layer")
        


# work with other services
def check_remaining_item(item_id: int, quantity: int) -> bool:
    with database.get_db() as db:

        storage_item = db.query(models.StorageItem.quantity)\
                            .join(models.Item)\
                            .where(models.StorageItem.item_id == item_id, \
                                    models.StorageItem.out_of_stock==False).first()
                                        
        # comparison between number of given quantity and quantity in Storage                        
        if storage_item.quantity < quantity: return False

        else: return True


def update_item_quantity(id: int, quantity: int): # update Item's quantity after taking out the Storage
    with database.get_db() as db:
        db.query(models.StorageItem)\
                .filter(models.StorageItem.item_id==id)\
                .update(
                        {models.StorageItem.quantity:models.StorageItem.quantity - quantity},
                        synchronize_session=False
                    )

        db.commit()

