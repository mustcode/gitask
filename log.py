from datetime import datetime

import settings

def timeStr():
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def add(msg):
    logFile = open(settings.LOG_FILE, 'a')
    logFile.write(timeStr() + '\t' + msg + '\n')
    logFile.close()

def clear():
    logFile = open(settings.LOG_FILE, 'w')
    logFile.close()
    print('logs cleared.')
