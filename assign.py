import sys
import os

import users
import tasks
import log

if len(sys.argv) < 4:
    print('error: expected 3-4 argument')
    print('usage: assign [-r|--remove] <path-to-task> <user> <role>')
    print('options:')
    print('-r : remove the specified assignment')
    sys.exit()

unassign = False
for i in range(len(sys.argv)):
    if sys.argv[i] != '-r' and sys.argv[i] != '--remove':
        continue
    unassign = True
    del sys.argv[i]
    break

sys.argv[0] = 'assign'
taskPath = sys.argv[1]
user = sys.argv[2]
role = sys.argv[3]

if not os.path.exists(taskPath):
    print('error: ' + taskPath + ' does not exist')
    sys.exit()

if not user in users.valid:
    print('error: user ' + user + ' does not exist')
    sys.exit()

try:
    role = tasks.Role[role]
except:
    print('error: role ' + role + ' does not exist')

if unassign:
    print("removing %s from role %s" % (user, role.name))
    tasks.unassign(taskPath, user, role, users.current)
else:
    print("assigning %s to role %s" % (user, role.name))
    tasks.assign(taskPath, user, role, users.current)
    
log.add(' '.join(sys.argv))
print('role assigned.')
