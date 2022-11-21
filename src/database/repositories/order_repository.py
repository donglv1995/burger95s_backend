from typing import List

from sqlalchemy.orm import joinedload

from src.burger95s.models import models
from src.burger95s.schemas import burger_schemas, order_schemas
from src.database import database


def get_orders():
    with database.get_db() as db:
        db_orders = db.query(models.Order)\
                        .options(joinedload(models.Order.ordering)).order_by(models.Order.id).all()

        return db_orders
        



# def get_orders_today(today: str=constant.TODAY_DATE):
#     with database.get_db() as db:
#         db_orders = db.query(models.Order)\
#                         .options(joinedload(models.Order.ordering))\
#                         .where(models.Order.ordered_date == today).all()

#         return db_orders




def get_consumer_orders(consumer: str):
    with database.get_db() as db:
        db_consumer_orders = db.query(models.Order)\
                                .options(joinedload(models.Order.ordering))\
                                .where(models.Order.consumer_name == consumer).all()

        return db_consumer_orders



def get_order_by_id(id: int):
    with database.get_db() as db:
        db_order = db.query(models.Order)\
                        .options(joinedload(models.Order.ordering))\
                            .where(models.Order.id == id).first()
        
        return db_order




def create_order(order: order_schemas.OrderCreate, id_burgers: List[int]) -> order_schemas.Order:
    with database.get_db() as db:
        new_order = models.Order(consumer_name=order.consumer_name)
        db.add(new_order)
        db.flush()

        latest_order = db.query(models.Order)\
                            .where(models.Order.id == new_order.id).first()

        for id in id_burgers:
            db_burger = db.query(models.Burger)\
                            .where(models.Burger.id == id).first()

            latest_order.ordering.append(db_burger)

        db.expire_on_commit = False
        db.commit()

        return latest_order




def update_order(update_order_id: int, order: order_schemas.Order, list_updated_burger_id: List[burger_schemas.Burger]):
     with database.get_db() as db:
        db_order = db.query(models.Order)\
                        .options(joinedload(models.Order.ordering))\
                        .where(models.Order.id == update_order_id).first()

        db_order.ordering.clear() # removes all given items
        db.flush()

        for id in list_updated_burger_id: # updates new items
            updated_burger = db.query(models.Burger)\
                                .options(joinedload(models.Burger.items))\
                                .where(models.Burger.id == id).first()

            db_order.ordering.append(updated_burger)

        db.commit()
        
        return db_order





def delete_order(id: int):
    with database.get_db() as db:
        db.query(models.Order)\
                .filter(models.Burger.id == id)\
                .update(
                        {models.Order.is_deleted: True},
                        synchronize_session=False
                    )
            
        db.expire_on_commit = False

        return db.query(models.Order).options(joinedload(models.Order.ordering)).where(models.Order.id == id).first()