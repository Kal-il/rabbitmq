import pika

class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.port = 5672
        self.username = "guest"
        self.password = "guest"
        self.queue = "data_queue"
        self.__callback = callback
        
    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host = self.__host,
            port = self.port,
            credentials = pika.PlainCredentials(
                username = self.username,
                password = self.password
            )
        )

        chanel = pika.BlockingConnection(connection_parameters).channel()
        chanel.queue_declare(
            queue = self.queue,
            durable = True
        )
        chanel.basic_consume(
            queue = self.queue,
            auto_ack=True,
            on_message_callback=self.__callback # uma ação condicional que será executada quando uma mensagem for recebida
        )
        
        return chanel
    
    def start_consuming(self):
        print(f"Listen rabbitmq on port 5672")
        self.__chanel.start_consuming() # inicia o processo de escuta do rabbitmq
        
def minha_callback(ch, method, properties, body):
    print(f"Received: {body}")   
    
    
rabbitmqconsumer = RabbitmqConsumer(minha_callback)
rabbitmqconsumer.start_consuming()