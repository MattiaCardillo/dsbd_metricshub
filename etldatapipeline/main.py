from flask import Flask
from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from datetime import timedelta
from confluent_kafka import Producer, Consumer
from prometheus_api_client.utils import parse_datetime
from configs import prometheus as prom_config
from configs import kafka as kafka_config

app = Flask(__name__)
prom = PrometheusConnect(url = prom_config.prometheushostname, disable_ssl=True)

def delivery_callback(err, msg):
        if err:
            print(err)
        else:
            print('kafka msg sended')

@app.route('/')
def hello():
    return 'Hello from Etl data pipeline'

@app.route('/metrics')
def getMetrics():
    allJobMetrics = prom.get_current_metric_value(metric_name= '', label_config = prom_config.label_config)
    return allJobMetrics

@app.route('/metrics/send')
def sendKafkaMetrics():
    # Create Producer instance
    p = Producer(**kafka_config.server_config)

    # Produce line (without newline)
    p.produce(kafka_config.kafka_topic, 'Prova msg', callback=delivery_callback)
    p.poll(0)
    p.flush()

    return 'Sended'

@app.route('/metrics/get')
def getKafkaMetrics():
    print('Consumer Start')
    c = Consumer({
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'prometheusgroup',
    'auto.offset.reset': 'earliest'
    })
    c.subscribe(['prometheusdata'])

    messageReceived = False;

    while (messageReceived == False):
        msg = c.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            print("Errore: {}".format(msg.error()))
            continue

        # Stampa il messaggio
        print("Messaggio ricevuto: {}".format(msg.value().decode('utf-8')))
        messageReceived = True
    c.close()

    return 'Received'


if __name__ == "__main__":
    app.run(host="0.0.0.0")