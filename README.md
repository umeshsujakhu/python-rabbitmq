## install python
## install pika
## install RabbitMQ

## Folders
- hello-world
  - contains simple text message exchange between producer and consumer
  - syntax : cd /hello-world
    - In different terminals : 
        - python3 receiver.py
        - python3 receiver.py
        - python3 send.py 
  - If multiple receiver is subscribing the sender then the message will be delivered in a
    Round Robin mechanism

- json-msg
  - contains json data exchange between producer and consumer
  - syntax : cd /json-msg
    - In different terminals : 
        - python3 receiver.py
        - python3 send.py 

- workers
  - contains message exchange between producer and consumer
  - syntax : cd /workers
    - In different terminals : 
        - python3 receiver.py
        - python3 receiver.py
        - python3 send.py Message1...
        - python3 send.py Message2.......
        - python3 send.py Message3...

  - the dots(.) after a message denotes the time in secondds to delay to test that 
    the messages are delivered to receiver only if it is free

- pub-sub
  - contains message exchange between producer and consumer
  - syntax : cd /pub-sub
    - In different terminals : 
        - python3 receiver.py
        - python3 receiver.py
        - python3 send.py Message1
        - python3 send.py Message2
        - python3 send.py Message3

  - the messages are delivered to every receivers at the same time