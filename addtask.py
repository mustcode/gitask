import sys
import os
import fileinput

import users
import tasks
import fields
import log

if len(sys.argv) == 1:
    taskName = input('enter task name: ')
else:
    del sys.argv[0]
    taskName = ' '.join(sys.argv)

if os.path.exists(tasks.path(taskName)):
    print('error: task already exists.')
    sys.exit()

print('adding task: ' + taskName)
taskPath = tasks.add(taskName)
fields.add(taskPath, fields.CREATED_BY, users.current)
log.add('addtask ' + taskName)
print('task added.')
