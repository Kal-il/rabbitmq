from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.port = 5672
        self.username = "guest"
        self.password = "guest"
        self.__exchange = "data_exchange"
        self.__routing_key = ""
        self.__chanel = self.__create_channel()
        
    def __create_channel(self):
        conneection_parameters = pika.ConnectionParameters(
            host = self.__host,
            port = self.port,
            credentials = pika.PlainCredentials(
                username = self.username,
                password = self.password
            )
        )

        channel = pika.BlockingConnection(conneection_parameters).channel()
        return channel
    
    def send_message(self, body: Dict):
         self.__chanel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
rabbitmqpublisher = RabbitmqPublisher()
rabbitmqpublisher.send_message({"message": "Hello World aaa!"})
                