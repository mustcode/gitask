import sys

import tasks
import users
import log

if len(sys.argv) < 3:
    print('error: expected 2 arguments')
    print('usage: comment <path-to-task> <comments>')
    sys.exit()

sys.argv[0] = 'comment'
taskPath = sys.argv[1]
comments = ' '.join(sys.argv[2:])

print("adding comment: " + comments)
tasks.comment(taskPath, users.current, comments)
log.add(' '.join(sys.argv))
print('comment added.')
