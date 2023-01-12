# compose_flask/app.py
from flask import Flask
import threading
import sys
sys.path.append("scripts/")
sys.path.append("configs/")
from scripts import startHelpers
from create_tables import startDb
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
startDb()

@app.route('/')
def hello():
    return 'Hello from Data storage'

@app.route('/start')
def kafkaStart():
    t = threading.Thread(target=startHelpers.startProcess)
    t.start()
    return 'Script started'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)