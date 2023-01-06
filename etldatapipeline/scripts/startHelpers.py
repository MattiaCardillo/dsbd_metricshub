from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from datetime import timedelta
import json
from confluent_kafka import Producer, Consumer
from prometheus_api_client.utils import parse_datetime
from configs import prometheus as prom_config
from scripts import prometheusHelpers
from scripts import kafkaHelpers
import threading

prom = PrometheusConnect(url = prom_config.prometheushostname, disable_ssl=True)

def startProcess():
    allJobMetrics = prometheusHelpers.getAllMetrics(prom=prom, prom_config=prom_config)
    # calculatedValues = {
    #     'metricsTrendOverTime': allJobMetrics[:3],
    #     'metrics1hData': allJobMetrics[3:5], #format will be: [{'metric': 'name, 'max': value, 'min': value, avg: value}]
    #     'metrics3hData': allJobMetrics[5:7], #format will be: [{'metric': 'name, 'max': value, 'min': value, avg: value}]
    #     'metrics12hData': allJobMetrics[7:9] #format will be: [{'metric': 'name, 'max': value, 'min': value, avg: value}]
    # }
    calculatedValues = {
        'metricsTrendOverTime': '',
        'metrics1hData': prometheusHelpers.getAllMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=1, metricList=allJobMetrics[:1]),
        'metrics3hData': prometheusHelpers.getAllMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=3, metricList=allJobMetrics[:1]),
        'metrics12hData': prometheusHelpers.getAllMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=12, metricList=allJobMetrics[:1]),
    }
    result = kafkaHelpers.sendKafkaMessage(json.dumps(calculatedValues))
    print('End start process')
