from confluent_kafka import Consumer
from scripts import kafkaHelpers

def startProcess():
    kafkaHelpers.startConsumeKafka()
    print('End start process')
