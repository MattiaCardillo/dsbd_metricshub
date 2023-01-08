import psycopg2

# Crea la connessione al database
conn = psycopg2.connect(host='localhost', port=5432, user='postgres', password='mypassword', dbname='postgres')

# Crea un cursore
cur = conn.cursor()

# Crea la tabella "users"
cur.execute("CREATE TABLE metrics (id SERIAL PRIMARY KEY, metric VARCHAR(255), max DOUBLE PRECISION, min DOUBLE PRECISION, avg DOUBLE PRECISION)")

# Committa le modifiche
conn.commit()

# Chiude la connessione
conn.close()