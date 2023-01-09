from confluent_kafka import Consumer
from configs import kafka as kafka_configs

def startConsumeKafka():
    #NB works only without docker
    print('Consumer Start')
    c = Consumer(kafka_configs.consumer_config)
    c.subscribe([kafka_configs.topic_name])

    try:
        while (True):
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            print('Received message: {}'.format(msg.value().decode('utf-8')))
        c.close()
    except Exception as e: 
        print(e)

    return