import os
import time
import shutil
import glob
from enum import Enum

import settings
import users
import fields
from status import Status
from role import Role
from action import Action

COMMENTS_DIR = 'comments'
ACTIVITY_DIR = 'activity'
ROLES_DIR = 'roles'

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
    __setStatus(taskPath, Status.requested)
    fields.add(taskPath, fields.Field.created_by, users.current)
    fields.add(taskPath, fields.Field.created_time, timeStr())
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
    __updateStatus(taskPath, action)

def addField(taskPath, user, field, value, replaceCurrentList = False):
    fields.add(taskPath, field, value, replaceCurrentList)
    update(taskPath, user, Action.add_field, [field, value])

def removeField(taskPath, user, field, value = None):
    fields.remove(taskPath, field, value)
    update(taskPath, user, Action.remove_field, [field, value])

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

def __updateStatus(taskPath, fromAction):
    assert isinstance(taskPath, str)
    assert fromAction in Action 

    if fromAction == Action.approve:
        __setStatus(taskPath, Status.backlog)
    elif fromAction == Action.reject:
        __setStatus(taskPath, Status.rejected)
    elif fromAction == Action.to_backlog:
        __setStatus(taskPath, Status.backlog)
    elif fromAction == Action.to_sprint:
        __setStatus(taskPath, Status.sprint)
    elif fromAction == Action.to_review:
        __setStatus(taskPath, Status.review)
    elif fromAction == Action.fail_review:
        __setStatus(taskPath, Status.fail)
    elif fromAction == Action.to_check:
        __setStatus(taskPath, Status.check)
    elif fromAction == Action.fail_check:
        __setStatus(taskPath, Status.fail)
    elif fromAction == Action.start_fix:
        __setStatus(taskPath, Status.fix)
    elif fromAction == Action.to_done:
        __setStatus(taskPath, Status.done)
    elif fromAction == Action.to_problem:
        __setStatus(taskPath, Status.problem)
    elif fromAction == Action.to_archive:
        __setStatus(taskPath, Status.arhived)

def __setStatus(taskPath, status):
    assert isinstance(taskPath, str)
    assert status in Status
    fields.add(taskPath, fields.Field.status, status)
