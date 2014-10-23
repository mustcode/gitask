import sys

import view
import fields

if len(sys.argv) < 2:
    print('error: expected at least 1 arguments')
    print('usage: viewtasks [-f|--flat] [<projects...>] <sort-field>')
    print('options:')
    print('-f : view result in flat view')
    sys.exit()

flatView = False
for i in range(len(sys.argv)):
    if sys.argv[i] != '-f' and sys.argv[i] != '--flat':
        continue
    flatView = True
    del sys.argv[i]
    break

if len(sys.argv) == 2:
    fromProjects = []
else:
    fromProjects = sys.argv[1:-1]
field = sys.argv[-1]

try:
    field = fields.Field[field]
except:
    print('error: ' + field + ' field does not exist')
    sys.exit()
    
print("from projects: " + str(fromProjects))
print("sort field: " + field.name)
view.show(fromProjects, field, flatView)
