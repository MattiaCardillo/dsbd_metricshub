import psycopg2
from config import postgre

# Crea la connessione al database
conn = psycopg2.connect(
        host=postgre.host,
        port=postgre.port,
        user=postgre.user,
        password=postgre.password,
        dbname=postgre.dbname,
    )

# Crea un cursore
cur = conn.cursor()

# Crea la tabella "users"
cur.execute("CREATE TABLE metrics (id SERIAL PRIMARY KEY, metric VARCHAR(255), max DOUBLE PRECISION, min DOUBLE PRECISION, avg DOUBLE PRECISION)")

# Committa le modifiche
conn.commit()

# Chiude la connessione
conn.close()