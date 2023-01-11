import os

bootstrap_server = 'kafka0:9092' if os.environ.get('isDocker') else 'localhost:29092'
consumer_config = {
    'bootstrap.servers': bootstrap_server,
    'group.id': 'grp',
    'auto.offset.reset': 'earliest'
}
topic_name = 'prometheusdata'