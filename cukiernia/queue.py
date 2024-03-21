import pika
from models import Order

#dodaje do kolejki queue_name
def push_to_queue(order: Order, queue_name):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=order.__repr__())
    
    connection.close()


def remove_from_queue(order: Order, queue_name):
    pass

def get_from_queue(queue_name) -> Order:
    pass
