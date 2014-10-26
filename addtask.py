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
tasks.add(taskName)
log.add('addtask ' + taskName)
print('task added.')
