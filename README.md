<img src="https://www.rabbitmq.com/img/rabbitmq-logo-with-name.svg" width="200"/>

### Nesse repositório estão os códigos feitos durante a playlist [RabbitMQ com Python](https://youtube.com/playlist?list=PLAgbpJQADBGLW5Q_OE86RzRb8HDvDzs-m&si=USij20ZyWe1PSrLn)

Paara rodar o projeto:
- Faça a instalação do Rabbitmq
- Crie uma maquina virtual
``` shell
python -m venv venv 
```
- Instale a biblioteca necessária
``` shell
pip  install pika
```
- Dê start no servidor:
``` shell
rabbitmqctl start
```
- Rode os programas


## Notas
RabbitMQ gerencia o **Protocolo AMQP**  (Advanced Method Queue Protocol)

Producer -> manda mensagem
Consumer -> consme mensagem   

(via de mão unica)

```
Producer --> Exchange --> Queue --> Consumer
                            ^          |
                            |__________|
                                ACK
```


