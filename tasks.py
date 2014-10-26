import os
import time
import shutil
from enum import Enum

import settings
import users

COMMENTS_DIR = 'comments'
ACTIVITY_DIR = 'activity'
ROLES_DIR = 'roles'

class Type(Enum):
    feature = 1
    improvement = 2
    issue = 3
    bug = 4
    workitem = 5

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

class Action(Enum):
    approve = 1
    reject = 2
    assign = 3
    unassign = 4
    to_backlog = 5
    to_sprint = 6
    start_work = 7
    finish_work = 8
    hold_work = 9
    resume_work = 10
    to_check = 11
    start_test = 12
    fail_test = 13
    start_fix = 14
    to_done = 15
    to_archive = 16

class Role(Enum):
    owner = 1
    implementer = 2
    designer = 3
    tester = 4
    reviewer = 5
    supervisor = 6
    observer = 7

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
    assert os.path.exists(taskPath)
    assert isinstance(author, str)
    assert isinstance(comments, str)

    commentsPath = taskPath + os.sep + COMMENTS_DIR
    if not os.path.exists(commentsPath):
        os.makedirs(commentsPath)

    commentTime = timeStr()
    commentFile = open(commentsPath + os.sep + commentTime + '-' + author + '.txt', 'w')
    commentFile.write(comments)
    commentFile.close()

def update(taskPath, user, action, params = None):
    assert isinstance(taskPath, str)
    assert os.path.exists(taskPath)
    assert isinstance(user, str)
    assert user in users.valid
    assert action in Action

    activityPath = taskPath + os.sep + ACTIVITY_DIR
    if not os.path.exists(activityPath):
        os.mkdir(activityPath)

    if params:
        assert isinstance(params, list)
        strParams = [None] * len(params)
        for i in range(0, len(params)):
            if isinstance(params[i], Enum):
                strParams[i] = params[i].name
            else:
                strParams[i] = str(params[i])
        activityName = action.name + '-' + '-'.join(strParams)
    else:
        activityName = action.name

    activityTime = timeStr()
    activityFile = open(activityPath + os.sep + activityTime + '-' + activityName + '-' + user, 'w')
    activityFile.close()

def assign(taskPath, user, role, assignBy):
    assert isinstance(taskPath, str)
    assert os.path.exists(taskPath)
    assert isinstance(user, str)
    assert isinstance(assignBy, str)
    assert user in users.valid
    assert assignBy in users.valid
    assert role in Role

    rolesPath = taskPath + os.sep + ROLES_DIR
    if not os.path.exists(rolesPath):
        os.mkdir(rolesPath)

    roleFile = open(rolesPath + os.sep + role.name + '-' + user, 'w')
    roleFile.close()
    update(taskPath, assignBy, Action.assign, [user, role])

def unassign(taskPath, user, role, unassignBy):
    assert isinstance(taskPath, str)
    assert os.path.exists(taskPath)
    assert isinstance(user, str)
    assert isinstance(unassignBy, str)
    assert user in users.valid
    assert unassignBy in users.valid
    assert role in Role

    rolesPath = taskPath + os.sep + ROLES_DIR
    assert os.path.exists(rolesPath)

    roleFile = rolesPath + os.sep + role.name + '-' + user
    os.remove(roleFile)
    update(taskPath, unassignBy, Action.unassign, [user, role])
