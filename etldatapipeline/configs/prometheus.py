prometheushostname="http://15.160.61.227:29090"
label_config = {'job': 'host'}
label_config2 = {'job': 'collector', "method":"put"}
label_config3 = {'job': 'collector', "method":"put", "quantile":"0.5"}
label_config4= {'job':"host",'__name__':"promhttp_metric_handler_requests_total", 'code':"200"}
selectedMetrics2 = [
    'node_timex_status',
    'go_memstats_heap_sys_bytes',
    'node_memory_Cached_bytes'
]
selectedMetrics = [
   {
    'name': 'promhttp_metric_handler_requests_total',
    'query': '{job="host",__name__="promhttp_metric_handler_requests_total", code="200"}'
   },
   {
    'name': 'pushgateway_http_push_duration_seconds',
    'query': '{job="collector", __name__="pushgateway_http_push_duration_seconds", quantile="0.5", method="put"}'

   }
]