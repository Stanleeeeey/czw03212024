from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from enum import Enum

db = declarative_base()

class Status(Enum):
    WAITING = 1
    PREPARATION = 2
    WAITING_FOR_DELIVERY = 3
    DELIVERED = 4

class Order(db):
    __tablename__ = "Orders" #nazwa tabelki

    id = Column(Integer, primary_key = True) #id zamowienia

    customer_name   = Column(String) #imie i nzawisko klienta
    customer_adress = Column(String) #adres dostawy

    ordered_food = Column(Integer) #id jedzenia zamowionego

    order_status = Column(String) #status zamowienia 

    def __repr__(self):
        return f'''
            id: {self.id},
            customer name: {self.customer_name},
            customer adress:{self.customer_adress},
            ordered_food: {self.ordered_food},
            order status: {self.order_status},
        '''

