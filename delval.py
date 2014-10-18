import sys
import os

import fields
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

if not fields.isValid(field):
    print('error: ' + field + 'is not a valid field')
    sys.exit()

if value:
    print("deleting value: " + value + ' in field: ' + field)
else:
    print("deleting field: " + field)

fields.remove(taskPath, field, value)
log.add(' '.join(sys.argv))
print('value deleted.')
