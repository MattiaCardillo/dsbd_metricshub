import psycopg2
from config import postgre

def connect():
    conn = psycopg2.connect(
        host=postgre.host,
        port=postgre.port,
        user=postgre.user,
        password=postgre.password,
        dbname=postgre.dbname,
    )
    return conn