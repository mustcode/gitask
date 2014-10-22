import os
import time
from enum import Enum

import settings

class Status(Enum):
    requested = 1
    rejected = 2
    backlog = 3
    sprint = 4
    doing = 5
    check = 6
    done = 7
    arhived = 8
    problem = 9

class Type(Enum):
    feature = 1
    improvement = 2
    issue = 3
    bug = 4
    workitem = 5

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

    commentTime = time.strftime('%Y%m%dT%H%M%S', time.gmtime())
    commentFile = open(commentsPath + os.sep + commentTime + '_by_' + author + '.txt', 'w')
    commentFile.write(comments)
    commentFile.close()
