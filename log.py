import settings

def add(msg):
    logFile = open(settings.LOG_FILE, 'a')
    logFile.write(msg + '\n')
    logFile.close()

def clear():
    logFile = open(settings.LOG_FILE, 'w')
    logFile.close()
    print('logs cleared.')
