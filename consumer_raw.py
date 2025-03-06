import pika

def my_callback(ch, method, properties, body):
    print(f"Received: {body}")

connection_parameters = pika.ConnectionParameters(
    host = "localhost",
    port = 5672,
    credentials = pika.PlainCredentials(
        username = "guest",
        password = "guest"
    )
)

chanel = pika.BlockingConnection(connection_parameters).channel()
chanel.queue_declare(
    queue = "data_queue",
    durable = True
)
chanel.basic_consume(
    queue = "data_queue",
    auto_ack=True,
    on_message_callback=my_callback # uma ação condicional que será executada quando uma mensagem for recebida
)

print(f"Listen rabbitmq on port 5672")
chanel.start_consuming() # inicia o processo de escuta do rabbitmq