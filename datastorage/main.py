# compose_flask/app.py
from flask import Flask
from confluent_kafka import Consumer
from scripts import kafkaHelpers

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Data storage'

@app.route('/start')
def kafkaStart():
    res = kafkaHelpers.startConsumeKafka()
    return res

if __name__ == "__main__":
    app.run(port=5001)