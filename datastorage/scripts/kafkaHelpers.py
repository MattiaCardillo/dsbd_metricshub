from confluent_kafka import Consumer
from config import kafka as kafka_configs

def startConsumeKafka():
    #NB works only without docker
    print('Consumer Start')
    c = Consumer(kafka_configs.consumer_config)
    c.subscribe([kafka_configs.topic_name])

    messageToRead = 1;
    messageReceived = 0;

    result = "Null"

    try:
        while (messageReceived<messageToRead):
            messageReceived +=1
            msg = c.poll(1.0)
            
            if msg is None:
                continue
            if msg.error():
                result = "Errore: {}".format(msg.error())
                continue

            # Stampa il messaggio
            result = "Messaggio ricevuto: {}".format(msg.value().decode('utf-8'))
        c.close()
    except(e): 
        print(e)

    return result