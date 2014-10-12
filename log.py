from datetime import datetime

import settings
import users

def timeStr():
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def add(msg):
    logFile = open(settings.LOG_FILE, 'a')
    logFile.write(timeStr() + ' ' + users.current + '\t' + msg + '\n')
    logFile.close()

def clear():
    logFile = open(settings.LOG_FILE, 'w')
    logFile.close()
    print('logs cleared.')
