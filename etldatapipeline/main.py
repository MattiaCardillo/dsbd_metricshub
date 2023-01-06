from flask import Flask, request, Response, make_response
import threading
from scripts import startHelpers
from scripts import logsHelpers
import datetime

# get the current date
now = datetime.datetime.now()
now_str = now.strftime('%d_%m_%Y')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Etl data pipeline'

@app.route('/start')
def sendKafkaMetrics():
    t = threading.Thread(target=startHelpers.startProcess)
    t.start()
    return 'Script started'
    
@app.route('/logs')
def getLogs():
    date = request.args.get('date')
    if date is None:
        date = now_str
    try:
        logs = logsHelpers.getLogFileByDate(date)
    except Exception as e:
        response = make_response('No valid date')
        response.status_code = 404
        return response
    return Response(logs, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0")