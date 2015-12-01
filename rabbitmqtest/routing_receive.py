#!/usr/bin/env python
# coding=utf8

import pika
import logging
import sys

log = logging.getLogger(__name__)

# Logging
logging.basicConfig(format='%(asctime)s: %(name)s --> %(message)s', level=logging.WARNING)


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    # log.warning("[x] received %r", body)
    # time.sleep(5)
    # print "[x] Done"
    # ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# define the exchange
channel.exchange_declare(exchange='MSG', type='direct')

routings = sys.argv[1:]
if not routings:
    routings = ['info']

# random get a queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
# bind the queue to consume data
for routing in routings:
    channel.queue_bind(exchange='MSG', queue=queue_name, routing_key=routing)

# fair to fetch the task
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name, no_ack=True)
log.warning("[*] Waiting for the message, to exit press ctrl+c")

channel.start_consuming()
