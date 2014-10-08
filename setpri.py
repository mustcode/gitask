import sys

import priority
import log

if len(sys.argv) != 4:
    print('error: expected 3 arguments')
    print('usage: setpri [path/to/task/dir] [urgency(0-9)] [importance(0-9)]')
    sys.exit()

sys.argv[0] = 'setpri'
taskPath = sys.argv[1]
urgency = int(sys.argv[2])
importance = int(sys.argv[3])

print('setting priority [%d%d] for task: %s' % (urgency, importance, taskPath))
priority.setPriority(taskPath, urgency, importance)
log.add(' '.join(sys.argv))
print('priority set.')
