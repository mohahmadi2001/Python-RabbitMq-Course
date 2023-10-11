import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="direct_log",exchange_type="direct")

message ={
    "Info":"this is info massage",
    "Error":"this is error massage",
    "warning":"this is warning massage"
}


for k,v in message.items():
    ch.basic_publish(exchange="direct_log",routing_key=k,body=v)

connection.close()