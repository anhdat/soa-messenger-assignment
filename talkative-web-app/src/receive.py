import pika
import time


def test_callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def message_listen(callback):
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
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    print(' [*] Waiting for messages.')
    channel.start_consuming()
