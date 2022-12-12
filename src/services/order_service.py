from src.burger95s import constant
from src.burger95s.models import models
from src.burger95s.schemas import order_schemas
from src.database.repositories import order_repository, burger_repository, item_repository
from src.services import burger_service


def get_orders():
    try:
        db_orders = order_repository.get_orders()

        return db_orders
    except:
        raise Exception(constant.RAISE_ERROR_STR)

# def get_orders_today(today: str = constant.TODAY_DATE):
#     try:
#         today_orders = order_repository.get_orders_today(today=today)

#     except Exception as e: 
#         raise Exception(constant.RAISE_ERROR_STR) e

#     return today_orders



def get_consumer_orders(consumer: str):
    try:
        consumer_orders = order_repository.get_consumer_orders(consumer=consumer)

        return consumer_orders
    except:
        raise Exception(constant.RAISE_ERROR_STR)



def create_order(order: order_schemas.OrderCreate):
    list_items =  []
    id_burgers = []
    item_quantity_dict = {}

    for burger in order.ordering: # collect all items from burgers
        list_items.extend(burger.items)

    for item in list_items: # create key-value repr for id: quantity
        if item_quantity_dict.get(item.item_id) is None:
            item_quantity_dict[item.item_id] = item.quantity
        
        else:
            item_quantity_dict[item.item_id] += item.quantity
        
    try:
        for id in item_quantity_dict.keys(): # check quantity of items in storage, 
            if not item_repository.check_remaining_item(item_id=id, quantity=item_quantity_dict[id]):
                raise Exception(f'there is not enough quantity of item ID: {id}')
            
        for burger in order.ordering: # check ID of burger, then collect all the IDs
            if burger.id == -1: # create a new one if ID -1
                new_burger = burger_repository.create_burger(burger=burger)
                id_burgers.append(new_burger.id)
            else:
                id_burgers.append(burger.id)
        
        # after all the checker finished and items are available, then create a new order 
        new_order = order_repository.create_order(order=order, id_burgers=id_burgers)

        for id in item_quantity_dict.keys(): # updating storage after created the order
            item_repository.update_item_quantity(id=id, quantity=item_quantity_dict[id])

        return new_order

    except:
        raise Exception(constant.RAISE_ERROR_STR)



def update_order(update_order_id: int, order: order_schemas.Order):
    list_burger_id = []
    
    try:
        # get order from database
        db_order = order_repository.get_order_by_id(update_order_id) 
        
        # update every single ones, then collect updated burger's ID
        for burger in db_order.orderding:
            updated_burger = burger_service.update_burger(burger=burger)
            list_burger_id.append(updated_burger.id)
        
        # update the order
        updated_order = order_repository.update_order(update_order_id, order=order, list_updated_burger_id=list_burger_id)

        return updated_order

    except:
        raise Exception(constant.RAISE_ERROR_STR) 

        

def delete_order(id: int): # soft deletion
    try:
        return order_repository.delete_order(id)
    
    except:
        raise Exception(constant.RAISE_ERROR_STR)