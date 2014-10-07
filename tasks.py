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

def add(taskName):
    dirName = taskName.replace(' ', '_')
    taskPath = settings.TASKS_DIR + os.sep + dirName
    assert not os.path.exists(taskPath)
    os.makedirs(taskPath)
    return taskPath
