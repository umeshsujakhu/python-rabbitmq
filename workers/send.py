import pika
import sys
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# declare queue named in config file
# durable true means even if rabbitmq server goes down before consumer consumes message, message will not be lost
channel.queue_declare(queue=cfg.QUEUE_TOPIC_WORKER, durable=True)

# get message from user else send `Hello World!`
# Example: python send.py Message1
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key=cfg.QUEUE_TOPIC_WORKER,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()