from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from datetime import timedelta
import json
from confluent_kafka import Producer, Consumer
from prometheus_api_client.utils import parse_datetime
from configs import prometheus as prom_config
from scripts import prometheusHelpers
from scripts import kafkaHelpers
from scripts import tsManipulationHelpers
from scripts import reportsHelpers

prom = PrometheusConnect(url = prom_config.prometheushostname, disable_ssl=True)

def startProcess():
    #Step 1 = calcoli un set di metadati con i relativi valori (autocorrelazione? stazionarietà? stagionalità?)
    result = firstStep()

    #Step 2 = calcoli il valore di max, min, avg, dev_std della metriche per 1h,3h, 12h;
    calculatedValues = secondStep()

    #Step 3 = calcoli il valore di max, min, avg, dev_std della metriche per 1h,3h, 12h;
    result = kafkaHelpers.sendKafkaMessage(json.dumps(calculatedValues))
    print('End start process')

def firstStep():
    print('Start first step \n')

    for metricName in prom_config.selectedMetrics:
        print('Start test on {}'.format(metricName))
        result = prometheusHelpers.getCustomMetricListRangeByHour(prom=prom, prom_config=prom_config, hour=24, metricName=metricName)
        ts = tsManipulationHelpers.parseIntoSeries(result[0]['values'])
        stationarityResult = tsManipulationHelpers.stationarityTest(ts)
        seasonabilityResult = tsManipulationHelpers.seasonabilityTest(ts)
        autocorrelationResult = tsManipulationHelpers.autocorrelationTest(ts)

        reportsHelpers.writeReport(metricName, ['Test di stazionarietà:', stationarityResult, 'Test di stagionalità:', seasonabilityResult, 'Test di autocorrelazione:' ,autocorrelationResult])

    print('End of the first step \n')
    return


def secondStep():
    print('Start second step \n')

    calculatedValues = {
        'metrics1hData': prometheusHelpers.getCustomMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=1, metricName="go.*"),
        'metrics3hData': prometheusHelpers.getCustomMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=3, metricName="go.*"),
        'metrics12hData': prometheusHelpers.getCustomMetricsRangeByHour(prom=prom, prom_config=prom_config, hour=12, metricName="go.*"),
    }

    print('End of the second step\n')
    return calculatedValues
