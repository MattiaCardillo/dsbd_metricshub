import mysql.connector
import os

host = 'host.docker.internal' if os.environ.get('isDocker') else 'localhost'

def startDb():
  # Crea la connessione al database
  mydb = mysql.connector.connect(
    host=host,
    user= os.environ.get('MYSQL_USER'),
    password= os.environ.get('MYSQL_ROOT_PASSWORD'),
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
    host=host,
    user= os.environ.get('MYSQL_USER'),
    password= os.environ.get('MYSQL_ROOT_PASSWORD'),
    database=os.environ.get('MYSQL_DB') 
  )
  mycursor = mydb.cursor()

  mycursor.execute(query)
  mydb.commit()

  query = """
  CREATE TABLE IF NOT EXISTS metrics1h (
      id INT NOT NULL AUTO_INCREMENT,
      metric VARCHAR(255),
      max DOUBLE,
      min DOUBLE,
      avg DOUBLE,
      std_dev DOUBLE,
      PRIMARY KEY (id)
  )
  """

  query2 = """
  CREATE TABLE IF NOT EXISTS metrics3h (
      id INT NOT NULL AUTO_INCREMENT,
      metric VARCHAR(255),
      max DOUBLE,
      min DOUBLE,
      avg DOUBLE,
      std_dev DOUBLE,
      PRIMARY KEY (id)
  )
  """

  query3 = """
  CREATE TABLE IF NOT EXISTS metrics12h (
      id INT NOT NULL AUTO_INCREMENT,
      metric VARCHAR(255),
      max DOUBLE,
      min DOUBLE,
      avg DOUBLE,
      std_dev DOUBLE,
      PRIMARY KEY (id)
  )
  """
  mycursor.execute(query)
  mycursor.execute(query2)
  mycursor.execute(query3)

  mydb.commit()

  mydb.close()
  return;