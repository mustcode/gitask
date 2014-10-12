import os
from datetime import datetime

import settings

SUBMITTED = 'submitted'
APPROVED = 'approved'
REJECTED = 'rejected'
BACKLOG = 'backlog'
SPRINT = 'sprint'
DOING = 'doing'
CHECK = 'check'
DONE = 'done'
ARCHIVED = 'arhived'
PROBLEM = 'problem'

status = [SUBMITTED, APPROVED, REJECTED, BACKLOG, SPRINT, DOING, CHECK, DONE, ARCHIVED, PROBLEM]

FEATURE = 'feature'
IMPROVEMENT = 'improvement'
ISSUE = 'issue'
BUG = 'bug'
WORKITEM = 'workitem'

types = [FEATURE, IMPROVEMENT, ISSUE, BUG, WORKITEM]

def path(taskName):
    dirName = taskName.replace(' ', '_')
    return settings.TASKS_DIR + os.sep + dirName

def add(taskName):
    taskPath = path(taskName)
    assert not os.path.exists(taskPath)
    os.makedirs(taskPath)
    
    descFile = open(taskPath + os.sep + 'description.txt', 'w')
    descFile.write('write description for this task here...')
    descFile.close()
    commentsPath = taskPath + os.sep + 'comments'
    os.makedirs(commentsPath)

    return taskPath

def comment(taskPath, author, comments):
    assert isinstance(taskPath, str)
    assert isinstance(author, str)
    assert isinstance(comments, str)

    commentsPath = taskPath + os.sep + 'comments'
    if not os.path.exists(commentsPath):
        os.makedirs(commentsPath)

    commentTime = datetime.now().strftime('%Y%m%dT%H%M%S')
    commentFile = open(commentsPath + os.sep + commentTime + '_by_' + author + '.txt', 'w')
    commentFile.write(comments)
    commentFile.close()
