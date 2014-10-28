import sys
import os

import fields
import tasks
import users
import log

argvCount = len(sys.argv)
if argvCount != 3 and argvCount != 4:
    print('error: expected 2-3 arguments')
    print('usage: delval <path-to-task> <field> [<value>]')
    sys.exit()

sys.argv[0] = 'delval'
taskPath = sys.argv[1]
field = sys.argv[2]
if argvCount == 4:
    value = sys.argv[3]
else:
    value = None

if not os.path.exists(taskPath):
    print('error: ' + taskPath + ' does not exist')
    sys.exit()

try:
    field = fields.Field[field]
except:
    print('error: ' + field + ' field does not exist')
    sys.exit()
try:
    value = fields.dataType(field)[value]
except:
    pass

if not fields.isValid(field):
    print('error: ' + field + 'is not a valid field')
    sys.exit()

if value:
    print("deleting value: " + str(value) + ' in field: ' + field.name)
else:
    print("deleting field: " + field.name)

tasks.removeField(taskPath, users.current, field, value)
log.add(' '.join(sys.argv))
print('value deleted.')
