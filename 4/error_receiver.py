import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="direct_log",exchange_type="direct")
result = ch.queue_declare(queue="",exclusive=True)
qname = result.method.queue

severity = "error"

ch.queue_bind(exchange="direct_log",queue=qname,routing_key=severity)
    
print("waiting for message")

def callback(ch, method, properties, body):
    with open("error_log.log", "a") as el:
        el.write(str(f"{body}") + "\n")
    
ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)

ch.start_consuming()