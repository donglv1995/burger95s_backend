from typing import List
from fastapi import APIRouter
from src.services import item_service
from src.burger95s.schemas import item_schemas

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "NOT Found"}}
)



# Create new Item

@router.post('/', response_model = item_schemas.Item)
def create_item(item: item_schemas.ItemCreate):
    return item_service.create_new_item(item=item)

# Get Item

@router.get('/', response_model = List[item_schemas.Item])
def get_items():
    return item_service.get_items()



@router.get('/{id}', response_model = item_schemas.Item)
def get_an_item_by_id(item_id: int):
    return item_service.get_item_by_id(id=item_id)


# Update Item

@router.put('/{id}')
def update_item(item: item_schemas.Item):
    updated = item_service.update_item_storage(item=item)
    if updated > 0:
        return "Item has been updated !"


# Delete Item (softed deletion)

@router.put('/{id}/delete')
def delete_item(id: int):
    deleted = item_service.delete_item(id=id)
    if deleted > 0:
        return "Item has been deleted !"



    