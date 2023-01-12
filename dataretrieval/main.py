# compose_flask/app.py
from flask import Flask
import sys
sys.path.append("scripts/")
from dotenv import load_dotenv

load_dotenv()
from scripts import dbHelpers
from create_tables import startDb

app = Flask(__name__)
startDb()

@app.route('/')
def hello():
    return 'Hello from Data retrieval'

@app.route('/listmetrics')
def getNames():
    result = dbHelpers.makeQuery(dbHelpers.queries['createView'], None)
    result = dbHelpers.makeQuery(dbHelpers.queries['listAllNames'], None)
    return result

@app.route('/metrics')
def getMetrics():
    result = dbHelpers.makeQuery(dbHelpers.queries['createView'], None)
    result = dbHelpers.makeQuery(dbHelpers.queries['getMetrics'], None)
    return result

@app.route('/metrics/<name>')
def getMetricsbyName(name):
    result = dbHelpers.makeQuery(dbHelpers.queries['createView'], None)
    if not name:
        result = dbHelpers.makeQuery(dbHelpers.queries['getMetrics'], None)
        return result
    result = dbHelpers.makeQuery(dbHelpers.queries['getMetricsByName'], (name,))
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)