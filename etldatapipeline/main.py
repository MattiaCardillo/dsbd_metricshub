from flask import Flask, request, Response, make_response, jsonify
import base64
import sys
sys.path.append("scripts/")
sys.path.append("configs/")
sys.path.append("logs/")
sys.path.append("reports/")

from scripts import analyticsHelpers
from scripts import logsHelpers
import datetime

# get the current date
now = datetime.datetime.now()
now_str = now.strftime('%d_%m_%Y')

app = Flask(__name__)

analyticsHelpers.startProcess()

@app.route('/')
def hello():
    return 'Hello from Etl data pipeline'

@app.route('/start')
def sendKafkaMetrics():
    result = analyticsHelpers.startProcess()
    return result
    
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

@app.route('/reports/<name>')
def get_file(name):
    encoded_string = ""
    try:
        with open('reports/'+name+'.pdf', "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
            encoded_string = encoded_string.decode('utf-8')
            apistatus="OK"
    except Exception as e:
        apistatus="KO"

    return jsonify(status=apistatus, encoded_pdf=encoded_string)

if __name__ == "__main__":
    app.run(host="0.0.0.0")