#!/usr/bin/env python
import pika


def main():
    # instance of the connection localhost with pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # create queue to receive messages
    channel.queue_declare(queue='hello')

    # function to receive message and printing
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # warning RabbitMQ that a callback function receives messages from the 'hello' queue
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
