from typing import List

from fastapi import APIRouter

from src.burger95s import constant
from src.burger95s.schemas import order_schemas
from src.services import order_service

router = APIRouter(
    prefix='/orders',
    tags=['orders'],
    responses={404: {"description": "NOT Found"}}
    
)

# Create order
@router.post('/', response_model=order_schemas.Order)
def create_order(order: order_schemas.OrderCreate):
    return order_service.create_order(order=order)


# Get order(s)
@router.get('/',response_model=List[order_schemas.Order])
def get_orders():
    return order_service.get_orders()



# @router.get('/today', response_model=List[order_schemas.Order])
# def get_orders_today(today: str=constant.TODAY_DATE):
#     return order_service.get_orders_today(today=today)




@router.get('/name', response_model=List[order_schemas.Order])
def get_consumer_orders(consumer: str):
    return order_service.get_consumer_orders(consumer=consumer)



# Update order
@router.put('/{id}/update', response_model=order_schemas.Order)
def update_order(update_order_id: int, order: order_schemas.Order):
    return order_service.update_order(update_order_id, order=order)




# Delete order
@router.put('/{id}/delete', response_model=order_schemas.OrderDeleted)
def delete_order(id: int):
    return order_service.delete_order(id)



