from src.burger95s.models import models
from src.burger95s.schemas import burger_schemas
from src.database import database
from src.burger95s import constant


def get_original_burgers():
    with database.get_db() as db:

        db_burger = db.query(models.Burger)\
                        .order_by(models.Burger.id).all()

        db.expunge_all()
        return db_burger
        



def get_original_burger_by_id(burger_id: int):
    with database.get_db() as db:

        db_burger = db.query(models.Burger)\
                        .order_by(models.Burger.id)\
                        .where(models.Burger.id == burger_id).first()

        return db_burger

  
def create_burger(burger: burger_schemas.Burger):
    with database.get_db() as db:

        new_burger = models.Burger(name=burger.name, type=constant.BURGER_TYPE_CUSTOME)
        
        for item in burger.items:
            db_item = db.query(models.Item).where(models.Item.id == item.item_id).first()
            new_burger.items.append(models.BurgerItemAssociation(item=db_item, quantity=item.quantity))
        
        db.add(new_burger)
        db.expire_on_commit = False
        db.commit()

        print("create burger successfully")
        return new_burger


def update_burger(update_burger_id: int, burger: burger_schemas.Burger):
    with database.get_db() as db:

        db_burger = db.query(models.Burger)\
                        .where(models.Burger.id == update_burger_id).first()

        db_burger.items.clear() # removes all given items
        db.flush()

        for item in burger.items: #updates new items to the burger 
            new_item = db.query(models.Item).where(models.Item.id == item.item_id).first()
            db_burger.items.append(models.BurgerItemAssociation(item=new_item, quantity=item.quantity))
        
        db.expire_on_commit = False
        db.commit()

        # updated_burger = db.query(models.Burger).where(models.Burger.id == update_burger_id).first()

        return db_burger
            

def delete_burger(id: int):
    with database.get_db() as db:
        try:
            db_burger = db.query(models.Burger)\
                            .filter(models.Burger.id==id)\
                            .update(
                                    {models.Burger.is_deleted: True},
                                    synchronize_session=False
                                )

            db.commit()

            return db_burger        
        
        except :
            raise Exception
    