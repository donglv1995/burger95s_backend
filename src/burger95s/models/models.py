import datetime
from typing import Union

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Table)
from sqlalchemy.orm import relationship

from src.burger95s import constant
from src.database.database import Base

order_burgers = Table( 'order_burgers',
                    Base.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('order_id',Integer, ForeignKey('orders.id')),
                    Column('burger_id',Integer, ForeignKey('burgers.id')),
                    
)



class BurgerItemAssociation(Base):
    __tablename__ = 'burger_items'
    id = Column(Integer, primary_key=True)
    burger_id = Column(Integer, ForeignKey('burgers.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    burger = relationship('Burger', back_populates='items')
    item = relationship('Item')


    def __init__(self, item, quantity):
        self.item = item
        self. quantity = quantity 

########################################
class Order(Base):
    __tablename__= 'orders'

    id = Column(Integer, primary_key=True, unique=True)
    consumer_name = Column(String(150), nullable=False)
    ordered_date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    is_deleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Order number: {self.id}> <Consumer: {self.consumer_name} Ordered date: {self.ordered_date} Burgers: {self.ordering}>"
    

    ordering = relationship('Burger', secondary=order_burgers, back_populates='ordered')




# ##########################################
class Burger(Base):
    __tablename__= 'burgers'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(150), nullable=False)
    type = Column(String(100), nullable=False)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<id = {self.id}, name = {self.name}, items: {self.items}>"


    def __init__(self, name, type: Union[constant.BURGER_TYPE_ORIGINAL, constant.BURGER_TYPE_CUSTOME]):
        self.name = name
        self.type = type

    ordered = relationship('Order', secondary=order_burgers, back_populates='ordering')

    items = relationship("BurgerItemAssociation", cascade="all, delete-orphan", lazy='selectin', back_populates='burger')


############################################
class Item(Base):
    __tablename__= 'items'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"<id: {self.id}, name: {self.name}>"
    

    burgers = relationship('BurgerItemAssociation', back_populates='item')



class StorageItem(Base):
    __tablename__ = 'storage_items'

    item_id = Column(Integer, ForeignKey('items.id'),primary_key=True)
    quantity = Column(Integer, default=10)
    out_of_stock = Column(Boolean, default=False)
    
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"<id: {self.item_id}, quantity: {self.quantity}>"















