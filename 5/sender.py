import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="topic_log",exchange_type="topic")

message ={
    "error.warning.important":"this is an important massage",
    "error.warning.notimportant":"this is not an important massage",

}


for k,v in message.items():
    ch.basic_publish(exchange="topic_log",routing_key=k,body=v)

print("Sent")
connection.close()