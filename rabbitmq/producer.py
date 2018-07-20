import pika
import schedule
import time

urls = [ "http://ebay.to/1G163Lh" ]

print("* Connecting to RabbitMQ broker")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='pages')


# channel.basic_publish(
#     exchange='',
    # routing_key='pages',
    # body='Kapil is Testing: 1,2,3...'
# )


def produce():
    for url in urls:
        print("* Pushed: [%s]" % (url))
        channel.basic_publish(
            exchange='',
            routing_key='pages',
            body=url
        )

schedule.every(0.0001).seconds.do(produce)

while True:
    schedule.run_pending()
    time.sleep(1)

# print("* Done sending !")

connection.close()
