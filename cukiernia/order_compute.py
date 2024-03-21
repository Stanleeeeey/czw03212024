import datetime
from cukiernia.models import Order, OrderItem, Product
from cukiernia.db import DataBase
from cukiernia.queue import push_to_queue, get_from_queue

def submit_order_status(order_id: int, status: str):
    db = DataBase()
    order = db.get_by_id(order_id)
    order.status = status
    db.save(order)
    push_to_queue(order, 'delivery')