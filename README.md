# MetricsHub

## Requirements
- Operating system: Windows, MacOS or Linux
- [Docker](https://www.docker.com) version 20 or higher
- [Python](https://www.python.org) version 3.7 or higher

## Abstract
MetricsHub is an application that utilizes the microservices architecture to handle data processing, storage and retrieval from a prometheus server. The application consists of three microservices: "ETL Data Pipeline", "Data Storage", and "Data Retrieval". The ETL Data Pipeline microservice is responsible for collecting metrics from a Prometheus server and forwarding them to a Kafka server through a kafka producer. Additionally, it exposes a RESTful interface that provides an easy way to access reports and logs related to the metrics processing. The Data Storage microservice communicates with the Kafka server through a Kafka consumer and performs insertion queries on a MySql database using the data retrieved from Kafka. The Data Retrieval microservice retrieves data from the MySql database and exposes a RESTful interface for external clients to access the data. All microservices are running on Docker, allowing for easy deployment and scaling of the application. By separating the data processing and storage into distinct microservices, the application can handle high volumes of data while maintaining flexibility and scalability.

## Installation Commands

1. Clone the repository;
2. Install the dependencies:
    + flask
    + confluent_kafka
    + datetime
    + prometheus_api_client
    + statsmodels
    + reportlab
    + mysql-connector-python
    + python-dotenv
3. Start application Environment:
    +  ```cd dsbd_metricshub ``` 
    + docker-compose-up on "docker-compose.yml"
4. Start the microservices:
    + Locally:
        + #### ETL DATA PIPELINE:
            + ```cd dsbd_metricshub/etldatapipeline``` 
            + ```python main.py``` 
        + #### DATA STORAGE:
            + ```cd dsbd_metricshub/datastorage``` 
            + ```python main.py```
        + #### DATA RETRIEVAL:
            + ```cd dsbd_metricshub/dataretrieval``` 
            + ```python main.py```

    + Docker:
        + #### ETL DATA PIPELINE:
            + ```cd dsbd_metricshub/etldatapipeline``` 
            + docker-compose-up on "docker-compose.yml"
        + #### DATA STORAGE:
            + ```cd dsbd_metricshub/datastorage``` 
            + docker-compose-up on "docker-compose.yml"
        + #### DATA RETRIEVAL:
            + ```cd dsbd_metricshub/dataretrieval``` 
            + docker-compose-up on "docker-compose.yml"
5. Start using microservice with an http client (You can find a postman collections in "postman_collections" folder)

## Microservices Architecture

![Architecture](/architecture.png)

## More

A detailed tecnical report can be found in /docs.