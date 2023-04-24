import pika, sys
import json
sys.path.append('../')
import config as cfg

#Establish a rabbitmq connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# define a JSON data
data = [{  
    "id": 1,         
    "name": "Umesh Sujakhu",         
    "age": 29    
    },
    {  
        "id": 2,         
        "name": "John Doe",               
        "age": 32   
    }]

message = json.dumps(data) 

#Declare a queue, if not exist create one
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

#Publish a message to a queue named in config file
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] Sent data")
connection.close()