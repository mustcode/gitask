import sys
import os
from enum import Enum

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

try:
    field = fields.Field[field]
except:
    print('error: ' + field + ' field does not exist')
    sys.exit()
try:
    value = fields.dataType(field)[value]
except:
    pass

if not fields.isValid(field, value):
    print('error: ' + field.name + ' = ' + str(value) + ' is not a valid field/value pair')
    sys.exit()

print("setting field: %s = %s" % (field, value))
fields.add(taskPath, field, value)
log.add(' '.join(sys.argv))
print('value added.')
