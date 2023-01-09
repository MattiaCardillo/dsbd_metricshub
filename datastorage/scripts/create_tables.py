import mysql.connector
import os

host = 'host.docker.internal' if os.environ.get('isDocker') else 'localhost'

# Crea la connessione al database
mydb = mysql.connector.connect(
  host=host,
  user="root",
  password="hegr.TEeH.243"
)

# Crea il cursore
mycursor = mydb.cursor()

query = """
CREATE DATABASE IF NOT EXISTS metricsDb
"""
mycursor.execute(query)
mydb.commit()
mydb.close()

mydb = mysql.connector.connect(
  host="host.docker.internal",
  user="root",
  password="hegr.TEeH.243",
  database="metricsDb"
)
mycursor = mydb.cursor()

mycursor.execute(query)
mydb.commit()

query = """
CREATE TABLE IF NOT EXISTS metrics (
    id INT,
    nome VARCHAR(255)
)
"""

mycursor.execute(query)
mydb.commit()

# sqldirect = "INSERT INTO metrics (metric, max, min, avg) VALUES ('test', 3.23, 1.34, 2.34)"
sqldirect = """INSERT INTO metrics (id, nome) VALUES (1, 'pippo');"""
mycursor.execute(sqldirect)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
mycursor.execute("SELECT * FROM metrics;")
mydb.close()