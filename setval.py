import sys
import os

import fields
import log

if len(sys.argv) != 4:
    print('error: expected 3 arguments')
    print('usage: setval <path-to-task> <field> <value>')
    sys.exit()

sys.argv[0] = 'setval'
taskPath = sys.argv[1]
field = sys.argv[2]
value = sys.argv[3]

if not os.path.exists(taskPath):
    print('error: ' + taskPath + ' does not exist')
    sys.exit()

if not fields.isValid(field, value):
    print('error: ' + field + ' = ' + value + ' is not a valid field/value pair')
    sys.exit()

print("setting field: %s = %s" % (field, value))
fields.add(taskPath, field, value)
log.add(' '.join(sys.argv))
print('value added.')
