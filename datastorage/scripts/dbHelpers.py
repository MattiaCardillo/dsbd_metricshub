import mysql.connector
import os

queries = {
    "insertMetric1h": "INSERT INTO metrics1h (metric, max, min, avg) VALUES (%s, %s, %s, %s)",
    "insertMetric3h": "INSERT INTO metrics3h (metric, max, min, avg) VALUES (%s, %s, %s, %s)",
    "insertMetric12h": "INSERT INTO metrics12h (metric, max, min, avg) VALUES (%s, %s, %s, %s)",
    "getMetrics": "SELECT * from metrics"
}

def connectToDb():
    mydb = mysql.connector.connect(
        host="host.docker.internal",
        user= os.environ.get('MYSQL_USER'),
        password= os.environ.get('MYSQL_ROOT_PASSWORD'),
        database= os.environ.get('MYSQL_DB')
    )
    return mydb

def makeQuery(query, values):
    db = connectToDb()
    mycursor = db.cursor()

    mycursor.execute(query, values)

    db.commit()
    db.close()
    return