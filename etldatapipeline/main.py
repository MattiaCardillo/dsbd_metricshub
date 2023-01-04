from flask import Flask
from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from datetime import timedelta
from confluent_kafka import Producer, Consumer
from prometheus_api_client.utils import parse_datetime
from configs import prometheus

kafka_config = {'bootstrap.servers': 'kafka:9092'}
kafka_topic = 'prometheusdata'

app = Flask(__name__)
prom = PrometheusConnect(url=prometheus.prometheushostname, disable_ssl=True)

label_config = {'job': 'prometheus'}

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
    allMetrics = prom.all_metrics(label_config)
    return allMetrics

@app.route('/metrics/send')
def sendKafkaMetrics():
    # Create Producer instance
    p = Producer(**kafka_config)

    # Produce line (without newline)
    p.produce(kafka_topic, 'Prova msg', callback=delivery_callback)
    p.poll(0)
    p.flush()

    return 'Sended'

@app.route('/metrics/get')
def getKafkaMetrics():
    c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'prometheusgroup',
    'auto.offset.reset': 'earliest'
    })

    c.subscribe([kafka_topic])
    print(c)
    msg = c.poll(1.0)
    print(msg)
    c.close()

    return 'Received'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)