from typing import List
from fastapi import APIRouter

from src.burger95s.schemas import burger_schemas
from src.services import burger_service

router = APIRouter(
    prefix = '/burgers',
    tags= ['burgers'],
    responses= {404: {"description": "404 NOT Found"}},
)


# Create new burger
@router.post('/', response_model=burger_schemas.Burger)
def create_new_burger(burger: burger_schemas.Burger): # default ID: -1 
    return burger_service.create_burger(burger=burger)


# Get burger(s)
@router.get('/', response_model=List[burger_schemas.Burger])
def get_original_burgers():
    return burger_service.get_original_burgers()



@router.get('/{id}', response_model=burger_schemas.Burger)
def get_original_burger_by_id(id: int):
    return burger_service.get_original_burger_by_id(id=id)



# Update Burger
@router.put('/{id}/update', response_model=burger_schemas.Burger)
def update_burger(id: int, burger: burger_schemas.Burger):
    return burger_service.update_burger(update_burger_id=id, burger=burger)
    



# Delete burger
@router.put('/{id}/delete', response_model=burger_schemas.BurgerUpdated)
def delete_burger(id: int):
    return burger_service.delete_burger(id=id)

