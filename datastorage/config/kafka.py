bootstrap_server = 'localhost:29092'
consumer_config = {
    'bootstrap.servers': bootstrap_server,
    'group.id': 'prometheusgroup',
    'auto.offset.reset': 'earliest'
}
topic_name = 'prometheusdata'