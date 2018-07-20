import pika
import requests
from bs4 import BeautifulSoup

def handler(ch, method, properties, body):
    print("-> Starting: {0}".format(body))
    r= requests.get(body)
    soup = BeautifulSoup(r.text, "html.parser")
    print("-> Extracted: %s" % (soup.html.head.title))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("-> Done: [%s]" % (body))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

print("* Handling messages.")

channel.basic_consume(handler, queue='pages', no_ack=False)

channel.start_consuming()