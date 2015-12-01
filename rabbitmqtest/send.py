#!/usr/bin/env python
# coding=utf8

import pika
import logging
import argparse

log = logging.getLogger(__name__)


def send_msg(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=msg)
    log.warning("[x] sended message [%s]!", msg)
    connection.close()


if __name__ == "__main__":
    # Logging
    logging.basicConfig(format='%(asctime)s: %(name)s --> %(message)s', level=logging.WARNING)

    # Arguments
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    msg_parser = subparsers.add_parser("msg", help="Send messages from to messaging queue.")
    msg_parser.add_argument("text")

    args = parser.parse_args()

    if args.command == "msg":
        #log.info("infor %s", args.text)
        send_msg(msg=args.text)
