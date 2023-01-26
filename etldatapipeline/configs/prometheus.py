prometheushostname="http://15.160.61.227:29090"

label_config = {'job': 'host'}


selectedMetrics = [
   {
    'name': 'promhttp_metric_handler_requests_total',
    'query': '{job="host",__name__="promhttp_metric_handler_requests_total", code="200"}',
    'params': {
        'period': 350,
        'model': 'additive'
    }
   },
   {
    'name': 'pushgateway_http_push_duration_seconds',
    'query': '{job="collector", __name__="pushgateway_http_push_duration_seconds", quantile="0.5", method="put"}',
    'params': {
        'period': 500,
        'model': 'additive'
    }
   }
]