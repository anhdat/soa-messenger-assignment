import pika


def say_hello(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker', port=5672))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f"Sent: \"{message}\"")
    connection.close()
