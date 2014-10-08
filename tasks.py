import os

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
BUG = 'bug'
WORKITEM = 'workitem'

types = [FEATURE, IMPROVEMENT, BUG, WORKITEM]

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
    
    commentsFile = open(taskPath + os.sep + 'comments.txt', 'w')
    commentsFile.close()

    return taskPath
