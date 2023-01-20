import mysql.connector
import os

queries = {
    "getMetrics": "SELECT * from allmetricviewfinal",
    "createView": """
        CREATE OR REPLACE VIEW allmetricviewfinal AS 
        SELECT metrics1h.metric as name, 
        metrics1h.max as max1h, metrics3h.max as max3h, metrics12h.max as max12h,
        metrics1h.min as min1h, metrics3h.min as min3h, metrics12h.min as min12h,
        metrics1h.avg as avg1h, metrics3h.avg as avg3h, metrics12h.avg as avg12h,
        metrics1h.std_dev as std_dev1h, metrics3h.std_dev as std_dev3h, metrics12h.std_dev as std_dev12h
        FROM metrics1h
        JOIN metrics3h
        ON metrics1h.id = metrics3h.id
        JOIN metrics12h
        ON metrics1h.id = metrics12h.id;
    """,
    "getMetricsByName": "SELECT * from allmetricviewfinal WHERE name = %s",
    "listAllNames": "SELECT name from allmetricviewfinal",
    "getMetricsFromTable1h": "SELECT * from metrics1h",
    "getMetricsFromTable3h": "SELECT * from metrics3h",
    "getMetricsFromTable12h": "SELECT * from metrics12h"
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
    mycursor = db.cursor(dictionary=True)

    mycursor.execute(query, values)

    result = mycursor.fetchall()
    mycursor.close()
    db.close()
    return result