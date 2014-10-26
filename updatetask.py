import sys
import os

import users
import tasks
import log
from action import Action

if len(sys.argv) != 3:
    print('error: expected 2 argument')
    print('usage: updatetask <path-to-task> <action>')
    sys.exit()

sys.argv[0] = 'updatetask'
taskPath = sys.argv[1]
action = sys.argv[2]

if not os.path.exists(taskPath):
    print('error: ' + taskPath + ' does not exist')
    sys.exit()

try:
    action = Action[action]
except:
    print('error: action ' + action + ' does not exist')
    sys.exit()

print("updating task: %s by %s" % (action.name, users.current))
tasks.update(taskPath, users.current, action)
log.add(' '.join(sys.argv))
print('task updated.')
