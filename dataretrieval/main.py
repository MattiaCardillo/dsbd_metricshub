# compose_flask/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Data retrieval'

if __name__ == "__main__":
    app.run(port=5002)