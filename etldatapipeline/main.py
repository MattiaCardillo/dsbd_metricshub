# compose_flask/app.py
from flask import Flask
from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from datetime import timedelta

from prometheus_api_client.utils import parse_datetime

app = Flask(__name__)
prom = PrometheusConnect(url="http://host.docker.internal:9090", disable_ssl=True)
#prom = PrometheusConnect(url="http://15.160.61.227:29090", disable_ssl=True)

label_config = {'job': 'prometheus'}

@app.route('/')
def hello():
    return 'Hello from Etl data pipeline'

@app.route('/metrics')
def getMetrics():
    allMetrics = prom.all_metrics(label_config)
    return allMetrics

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)