from confluent_kafka import Consumer
from configs import kafka as kafka_configs
from scripts import dbHelpers
import json

def startConsumeKafka():
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
            metricMsg = msg.value().decode('utf-8')
            print('Received message: {}'.format(metricMsg))
            metricMsg = json.loads(msg.value().decode('utf-8'))
            for msg in metricMsg["metrics1hData"]:
                dbHelpers.makeQuery(dbHelpers.queries["insertMetric1h"], (msg["metric"], msg["max"], msg["min"], msg["avg"], msg['std_dev']))
            
            for msg in metricMsg["metrics3hData"]:
                dbHelpers.makeQuery(dbHelpers.queries["insertMetric3h"], (msg["metric"], msg["max"], msg["min"], msg["avg"], msg['std_dev']))
            
            for msg in metricMsg["metrics12hData"]:
                dbHelpers.makeQuery(dbHelpers.queries["insertMetric12h"], (msg["metric"], msg["max"], msg["min"], msg["avg"], msg['std_dev']))
        c.close()
    except Exception as e: 
        print(e)

    return