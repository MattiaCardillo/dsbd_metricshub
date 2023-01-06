from confluent_kafka import Producer
from configs import kafka as kafka_config

def delivery_callback(err, msg):
        if err:
            print(err)
        else:
            print('kafka msg sended')

def sendKafkaMessage(msg):
    # Create Producer instance
    p = Producer(**kafka_config.server_config)

    # Produce line (without newline)
    p.produce(kafka_config.kafka_topic, msg, callback=delivery_callback)
    p.poll(1)
    p.flush()

    return 'Sended'