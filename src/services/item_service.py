from src.burger95s.schemas import item_schemas
from src.database.repositories import item_repository
from src.burger95s import constant


def create_new_item(item: item_schemas.ItemCreate):
    try:
        created_item = item_repository.create_item(item=item)
        print(created_item)
        return created_item
        
    except:
         raise Exception(constant.RAISE_ERROR_STR)


def get_items():
    try:    
        items = item_repository.get_items()

        if items is None:
            raise Exception('There are no items in database')
        
        return items

    except:
        raise Exception(constant.RAISE_ERROR_STR)



def get_item_by_id(id: int):
    try:    
        item = item_repository.get_item_by_id( item_id=id)
        
        return item

    except :
        raise Exception(constant.RAISE_ERROR_STR)




def update_item_storage(item: item_schemas.Item):
    try:
        updated_item = item_repository.update_item_storage(item=item)

        print(f'Quantity of the item id {str(item.id)} has been updated')
        if updated_item > 0: return True

    except :
        raise Exception(constant.RAISE_ERROR_STR) 




def delete_item(id: int):
    try:
        return item_repository.delete_item_storage_by_id(item_id=id)
         

    except: raise Exception(constant.RAISE_ERROR_STR)

    