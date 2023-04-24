import pika
import json
import sys
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(cfg.RABBIT_HOST))
channel = connection.channel()

queue = channel.queue_declare(cfg.ORDER_REPORT_TOPIC)
queue_name = queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.report'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(' [x] Generating report')
    print(f"""
    ID: {payload.get('id')}
    User Email: {payload.get('user_email')}
    Product: {payload.get('product')}
    Quantity: {payload.get('quantity')}
    """)
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)

print(' [*] Waiting for report messages. To exit press CTRL+C')

channel.start_consuming()