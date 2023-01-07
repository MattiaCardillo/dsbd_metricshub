# compose_flask/app.py
from flask import Flask
import threading
from scripts import startHelpers

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Data storage'

@app.route('/start')
def kafkaStart():
    t = threading.Thread(target=startHelpers.startProcess)
    t.start()
    return 'Script started'

if __name__ == "__main__":
    app.run(port=5001)