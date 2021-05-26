#!/usr/bin/env python
import pika


def main(message: str = 'Hello World!'):
    # instance of the connection localhost with pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # create queue to receive messages
    channel.queue_declare(queue='hello')

    # exchange in the queue with empty string, sending message to the 'hello' queue
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent %r" % message)

    # closing connection
    connection.close()
