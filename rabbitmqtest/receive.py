#!/usr/bin/env python
# coding=utf8

import pika
import logging
import time

log = logging.getLogger(__name__)

# Logging
logging.basicConfig(format='%(asctime)s: %(name)s --> %(message)s', level=logging.WARNING)

def callback(ch, method, properties, body):
    log.warning("[x] received %r", body)
    time.sleep(5)
    print "[x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

# fair to fetch the task
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello', no_ack=False)
log.warning("[*] Waiting for the message, to exit press ctrl+c")

channel.start_consuming()
