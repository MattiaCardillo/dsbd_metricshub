import logging
import datetime

# get the current date
now = datetime.datetime.now()
date_str = now.strftime('%d_%m_%Y')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('logs/'+date_str+'.log')
handler.setFormatter(formatter)

# create a logger
logger = logging.getLogger('ETL Data Pipeline Logger')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def getLogger():
    return logger

def getLogFileByDate(date):
    filename = date+'.log'
    logs = ''
    with open('logs/'+filename, 'r') as f:
        logs = f.read()
    return logs

# log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message2')