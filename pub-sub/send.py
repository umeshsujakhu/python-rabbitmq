import pika
import sys
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare a exchange named in config file
channel.exchange_declare(exchange=cfg.EXCHANGE_TOPIC, exchange_type='fanout')

# Get message from user else send `info: Hello World!`
# Example: python send.py Message1
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange=cfg.EXCHANGE_TOPIC, routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()