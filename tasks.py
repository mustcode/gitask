import os
import time
import shutil
from enum import Enum

import settings

COMMENTS_DIR = 'comments'
ACTIVITY_DIR = 'activity'

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

class Action(Enum):
    approve = 1
    reject = 2
    assign_role = 3
    to_backlog = 4
    to_sprint = 5
    start_work = 6
    finish_work = 7
    hold_work = 8
    resume_work = 9
    to_check = 10
    start_test = 11
    fail_test = 12
    start_fix = 13
    to_done = 14
    to_archive = 15

def path(taskName):
    dirName = taskName.replace(' ', '_')
    return settings.TASKS_DIR + os.sep + dirName

def timeStr():
    return time.strftime('%Y%m%dT%H%M%S', time.gmtime())

def add(taskName):
    taskPath = path(taskName)
    assert not os.path.exists(taskPath)
    os.makedirs(taskPath)
    descFile = open(taskPath + os.sep + 'description.txt', 'w')
    descFile.write('write description for this task here...')
    descFile.close()
    return taskPath

def delete(taskPath):
    assert os.path.exists(taskPath)
    shutil.rmtree(taskPath)

def deleteAll():
    assert os.path.exists(settings.TASKS_DIR)
    shutil.rmtree(settings.TASKS_DIR)

def comment(taskPath, author, comments):
    assert isinstance(taskPath, str)
    assert isinstance(author, str)
    assert isinstance(comments, str)

    commentsPath = taskPath + os.sep + COMMENTS_DIR
    if not os.path.exists(commentsPath):
        os.makedirs(commentsPath)

    commentTime = timeStr()
    commentFile = open(commentsPath + os.sep + commentTime + '-' + author + '.txt', 'w')
    commentFile.write(comments)
    commentFile.close()

def update(taskPath, user, action):
    assert isinstance(taskPath, str)
    assert isinstance(user, str)
    assert action in Action

    activityPath = taskPath + os.sep + ACTIVITY_DIR
    if not os.path.exists(activityPath):
        os.mkdir(activityPath)

    activityTime = timeStr()
    activityFile = open(activityPath + os.sep + activityTime + '-' + action.name + '-' + user, 'w')
    activityFile.close()
