from typing import List
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.burger95s.schemas import item_schemas
from src.services.item_service import ItemService
from src.container.container import Container

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "NOT Found"}}
)



@router.get('/', response_model = List[item_schemas.Item])
@inject
def get_items(item_service: ItemService = Depends(Provide[Container.item_service]),):
    return item_service.get_items()


@router.get('/{id}/', response_model= item_schemas.Item)
@inject
def get_item_by_id(
    item_id: int,
    item_service: ItemService = Depends(Provide[Container.item_service])
):
    return item_service.get_item_by_id(item_id=item_id)


@router.post('/', response_model=item_schemas.Item)
@inject
def create_item(
    item: item_schemas.ItemCreate,
    item_service: ItemService = Depends(Provide[Container.item_service])
):
    return item_service.create_item(item=item)


@router.put('/{id}/', response_model=item_schemas.DeletedItem)
@inject
def delete_item(
    item_id: int,
    item_service: ItemService = Depends(Provide[Container.item_service])
):
    return item_service.soft_delete_item_by_id(item_id=item_id)




    