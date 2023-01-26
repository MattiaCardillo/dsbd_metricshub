from prometheus_api_client.utils import parse_datetime
from datetime import timedelta
from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from scripts import logsHelpers
import time
import numpy as np

def getAllMetrics(prom, prom_config):
    allJobMetrics = prom.get_current_metric_value(metric_name= '', label_config = prom_config.label_config)
    return allJobMetrics

def getAllMetricsRangeByHour(hour, prom, prom_config, metricList):
    start_time_second = time.time()

    start_time = parse_datetime(str(hour).join("h"))
    end_time = parse_datetime("now")
    chunk_size = timedelta(minutes=5)
    newMetricsArray = []
    newMetricsFormat = {'metric': None, 'max': None, 'min': None, 'avg': None}

    for metricData in metricList:
        print('Running for {}'.format(metricData['metric']['__name__']))
        metric_data = prom.get_metric_range_data(
            metric_name=metricData['metric']['__name__'],
            label_config=prom_config.label_config,
            start_time=start_time,
            end_time=end_time,
            chunk_size=chunk_size,
        )
        metric_df = MetricRangeDataFrame(metric_data)
        max= metric_df['value'].max()
        min= metric_df['value'].min()
        avg= metric_df['value'].mean()
        newMetricsFormat['metric'] = metricData['metric']['__name__']
        newMetricsFormat['max'] = max
        newMetricsFormat['min'] = min
        newMetricsFormat['avg'] = avg
        newMetricsArray.append(newMetricsFormat)

    end_time = time.time()
    duration = end_time - start_time_second
    logsHelpers.getLogger().info('{0}h scripts took {1} seconds to end'.format(hour, duration))

    return newMetricsArray

def getCustomMetricsRangeByHour(hour, prom, prom_config, metricName):
    start_time_second = time.time()
    query='{__name__=~"'+metricName+'",job="'+prom_config.label_config['job']+'"}['+str(hour)+'h]'
    metricList = prom.custom_query(query)

    newMetricsArray = []
    newMetricsFormat = {'metric': None, 'max': None, 'min': None, 'avg': None, 'std_dev': None}
    for metricData in metricList:
        print('Running for {}'.format(metricData['metric']['__name__']))
        
        metric_df = MetricRangeDataFrame(metricData)
        max= metric_df['value'].max()
        min= metric_df['value'].min()
        avg= metric_df['value'].mean()
        std_dev = np.std(metric_df['value'])

        newMetricsFormat['metric'] = metricData['metric']['__name__']
        newMetricsFormat['max'] = max
        newMetricsFormat['min'] = min
        newMetricsFormat['avg'] = avg
        newMetricsFormat['std_dev'] = std_dev   
        newMetricsArray.append(newMetricsFormat.copy())

    end_time = time.time()
    duration = end_time - start_time_second
    logsHelpers.getLogger().info('{0}h scripts took {1} seconds to end'.format(hour, duration))

    return newMetricsArray

def getCustomMetricListRangeByHour(hour, prom, label_config, metricName):
    query='{__name__=~"'+metricName+'",job="'+label_config['job']+'"}['+str(hour)+'h]'
    metricList = prom.custom_query(query)

    return metricList

def getCustomMetricListFromQuery(hour, prom, query):
    q=query+'['+str(hour)+'h]'
    metricList = prom.custom_query(q)

    return metricList