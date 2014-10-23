import sys
import os

import settings
import tasks
import log

if len(sys.argv) != 2:
    print('error: expected 1 argument')
    print('usage: deltask <path-to-task> | -a|--all')
    print('options:')
    print('-a : delete all tasks')
    sys.exit()

sys.argv[0] = 'deltask'
taskPath = sys.argv[1]

if taskPath == '-a' or taskPath == '--all':
    if not os.path.exists(settings.TASKS_DIR):
        print('no tasks to delete.')
        sys.exit()
    else:
        print('deleting all tasks')
        tasks.deleteAll()
else:
    print('deleting task: ' + taskPath)
    tasks.delete(taskPath)

log.add(' '.join(sys.argv))
print('task deleted.')