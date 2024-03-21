import pika
from models import Order

#dodaje do kolejki 'delivery' 
def push_to_delivery(order: Order):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='delivery')

    channel.basic_publish(exchange='',
                      routing_key='delivery',
                      body=order.__repr__())
    
    connection.close()


def remove_from_queue(order: Order):
    pass

def get_from_queue() -> Order:
    pass
