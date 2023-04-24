import pika, sys
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

channel.exchange_declare(exchange=cfg.EXCHANGE_TOPIC, exchange_type='fanout')

# declare a queue for exchange, which is done by rabbitmq itself
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue  # get the name of a queue declared by rabbitmq

channel.queue_bind(exchange=cfg.EXCHANGE_TOPIC, queue=queue_name) # bind the declared queue to a exchange named ``

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()