from src.burger95s import constant
from src.burger95s.schemas import burger_schemas
from src.database.repositories import burger_repository, item_repository


def get_original_burgers():
    try:
        original_burgers = burger_repository.get_original_burgers()
        return original_burgers
    
    except :
        raise Exception(constant.RAISE_ERROR_STR)





def get_original_burger_by_id(id: int):
    try:
        burger = burger_repository.get_original_burger_by_id(burger_id=id)

        return burger
    
    except :
        raise Exception(constant.RAISE_ERROR_STR)




def create_burger(burger: burger_schemas.Burger):
    try:
        id_quantity = {}
        for item in burger.items: # collect all items&quantity into a dict
            if id_quantity.get(item.item_id) is None:
                id_quantity[item.item_id] = item.quantity
            else:
                id_quantity[item.item_id] += item.quantity

        for id in id_quantity.keys(): # check quantity in the storage
            
            if not item_repository.check_remaining_item(item_id=id, quantity=id_quantity[id]): # raise immediately if not enough item
                raise (f'there only {id_quantity[id]} left, its not enough to make the burgers') 

        created_burger = burger_repository.create_burger(burger=burger)  # create a customization burger
        
        for id in id_quantity.keys(): # updating storage after created burger
            item_repository.update_item_quantity(id=id, quantity=id_quantity[id])

        return created_burger

    except :
        raise Exception(constant.RAISE_ERROR_STR)
    
        



def update_burger(update_burger_id: int,burger: burger_schemas.Burger):
    try:
        # get the burger we want to update
        db_burger = burger_repository.get_original_burger_by_id(burger_id=update_burger_id)

        # checking the type, if the given burger has the same type with db_burger, then
        if burger.type == db_burger.type == constant.BURGER_TYPE_ORIGINAL:

            original_burger = burger_repository.get_original_burger_by_id(burger_id=burger.id)
            burger_repository.delete_burger(id=update_burger_id) # delete the db_burger

            return original_burger

        # if it's not the same type, then we update the items
        else: return burger_repository.update_burger(update_burger_id=update_burger_id, burger=burger)
    
    except :
        raise Exception(constant.RAISE_ERROR_STR)



def delete_burger(id: int):
    try:
        return burger_repository.delete_burger(id=id)

    except :
        raise Exception(constant.RAISE_ERROR_STR)
    