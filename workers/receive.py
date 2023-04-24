import pika, sys
import time
sys.path.append('../')
import config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

channel.queue_declare(queue=cfg.QUEUE_TOPIC_WORKER, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))  # add timeout based on dots(.) in message Example: Message1... adds 3 seconds
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag) # Send acknowledgement instead of auto acknowledgement

# fetch only one task at a time
# if a worker is busy then meesage is delivered to next worker
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=cfg.QUEUE_TOPIC_WORKER, on_message_callback=callback)

channel.start_consuming()