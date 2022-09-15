
from http.client import HTTPException
from ..database.repositories import item_repository
from ..burger95s.dto.models.item_info import Item,ItemInfo

#by default, the key-value item_id in Item model is not in the right place, 
    # thus need to reorder that pair on Top to match with tuple values
def get_keys():
    item_keys = ["item_id"]
    keys = list(ItemInfo.__fields__.keys())
    item_keys.extend(keys)

    return item_keys

# mapping list of keys with a tuple values then return it in pydantic BaseModel
def convert_item_to_model(item, item_keys):
    item_dict = {key: item[i] for i, key in enumerate(item_keys)}
    item_base_model = Item(**item_dict)
    
    return item_base_model


def get_items():
    items = []
    final_result = []
    try:
        items = item_repository.get_items()
        item_keys = get_keys()
        for item in items:
            final_result.append(convert_item_to_model(item, item_keys))

    except:
        raise HTTPException("there something wrong with the try statement, please check it !")

    return final_result

def get_particular_items(type: str):
    items = []
    final_result = []
    try:
        items = item_repository.get_particular_items(type=type)
        item_keys = get_keys()
        for item in items:
            final_result.append(convert_item_to_model(item, item_keys))

    except:
        raise ValueError('Wrong Type, please filling in approriated type !')

    return final_result


def get_item_by_id(itemid):
    item = None

    try:
        item = item_repository.get_item_by_id(itemid=itemid)
        item_keys = get_keys()
        item = convert_item_to_model(item, item_keys)
    
    except:
        raise ValueError('Item not Found')
    
    return item


def create_item(item: ItemInfo):
    created_item = None

    try:
        created_item = item_repository.create_item(item=item)

    except:
        raise NotImplementedError('Cause some issues when creating new item, please check the properties again !')
        
    return created_item

def update_item(itemid, item: ItemInfo):
    updated_item = None
    try:
        updated_item = item_repository.update_item(itemid=itemid, item=item)
    
    except:
        raise NotImplementedError('Cause some issues when updating item, please check the properties again !')

    return updated_item

def delete_item(itemid, is_hard_delete):
    deleted_item = None
    try:
        deleted_item = item_repository.delete_item(itemid=itemid, is_hard_delete=is_hard_delete)

    except:
        raise ValueError('Item not found, Are you sure the item exists !')

    return deleted_item