import pika
import time


def say_hello(message):
    start_time = time.time()
    while True:
        # wait for rabbitmq
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='message-broker', port=5672))
            break
        except pika.exceptions.AMQPConnectionError:
            print('Cannot connect yet, sleeping 3 seconds.')
            time.sleep(3)
        if time.time() - start_time > 60:
            print('Could not connect after 30 seconds.')
            exit(1)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f"Sent: \"{message}\"")
    connection.close()
