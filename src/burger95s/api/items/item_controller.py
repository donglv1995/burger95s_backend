from typing import List
from fastapi import APIRouter, Query
from src.burger95s.dto.models.item_info import Item, ItemInfo
from src.services import item_service
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "NOT Found"}},
)

@router.get("/", response_model=List[Item]) # items/
async def get_items(type: str = Query(description='''
filling correctly which type of items do you want: All, Burger, Finger food, Extra''')):
    if type == 'All':
        return item_service.get_items()
    else:
        return item_service.get_particular_items(type=type)
    

@router.get("/{itemid}", response_model= Item) # /items/{itemid}
async def get_item(itemid):

    return item_service.get_item_by_id(itemid=itemid)


@router.post("/")
async def create_item(item: ItemInfo):

    return item_service.create_item(item=item)


@router.put("/{itemid}")
async def update_item(itemid, item: ItemInfo):

    return item_service.update_item(itemid=itemid, item=item)


@router.put("/{itemid}/{delete}")
async def delete_item(itemid, is_hard_delete: bool= False):
    
    return item_service.delete_item(itemid=itemid, is_hard_delete=is_hard_delete)
    