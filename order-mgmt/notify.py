import pika
import json
import sys
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(cfg.RABBIT_HOST))
channel = connection.channel()

queue = channel.queue_declare(cfg.ORDER_NOTIFY_TOPIC)
queue_name = queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(' [x] Notifying {}'.format(payload['user_email']))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)

print(' [*] Waiting for notify messages. To exit press CTRL+C')

channel.start_consuming()