import pika, sys, os
import json
sys.path.append('../')
import config as cfg


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

channel.queue_declare(queue=cfg.QUEUE_TOPIC)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):  
    # print("Method: {}".format(method))     
    # print("Properties: {}".format(properties))     
    data = json.loads(body)
    for d in data:
        print("ID: {}".format(d['id']))     
        print("Name: {}".format(d['name']))      
        print('Age: {}'.format(d['age']))
        print('\n')

channel.basic_consume(queue=cfg.QUEUE_TOPIC, on_message_callback=callback, auto_ack=True)


channel.start_consuming()
