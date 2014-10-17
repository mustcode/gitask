import sys
import os
import fileinput
import time

import users
import tasks
import fields
import log

if len(sys.argv) == 1:
    taskName = input('enter task name: ')
else:
    taskName = ' '.join(sys.argv[1:])

if os.path.exists(tasks.path(taskName)):
    print('error: task already exists.')
    sys.exit()

print('adding task: ' + taskName)
taskPath = tasks.add(taskName)
fields.add(taskPath, fields.CREATED_BY, users.current)
fields.add(taskPath, fields.CREATED_TIME, time.strftime('%Y%m%dT%H%M%S', time.gmtime()))
fields.add(taskPath, fields.STATUS, tasks.REQUESTED)
log.add('addtask ' + taskName)
print('task added.')
