from typing import List
from fastapi import APIRouter, Query, Body
from src.burger95s.models.item_info import ItemInfo
from src.burger95s.dto.item_user_dto import ItemInfoDTO
from src.services import item_service
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "NOT Found"}},
)

@router.get("/") # items/
async def get_items(type: str = Query(description='''
filling correctly which type of items do you want: All, Burger, Finger food, Extra''')):
    if type == 'All':
        return item_service.get_items()
    else:
        return item_service.get_particular_items(type=type)
    

@router.get("/{itemid}") # /items/{itemid}
async def get_item(itemid):

    return item_service.get_item_by_id(itemid=itemid)


@router.post("/")
async def create_item(item: ItemInfo):

    return item_service.create_item(item=item)


@router.put("/{itemid}")
async def update_item(itemid, item: ItemInfo = Body(
    example={
    "item_name": 'sandwich',
    "price": 35000,
    "type": "Burger",
    "size": 'M'
})):

    return item_service.update_item(itemid=itemid, item=item)


@router.put("/{itemid}/{delete}")
async def delete_item(itemid, is_hard_delete: bool= False):
    
    return item_service.delete_item(itemid=itemid, is_hard_delete=is_hard_delete)
    