import pika, sys
sys.path.append('../')
import config as cfg

#Establish a rabbitmq connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

#Declare a queue, if not exist create one
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

#Publish a message to a queue named in config file
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body='Hello World')
print(" [x] Sent 'Hello World'")
connection.close()