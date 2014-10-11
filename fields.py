import sys
import os
import glob
import shutil

import users
import tasks
import projects
import teams
import priority
import complexity

CREATED_BY = 'created_by'
CREATED_TIME = 'created_time'
PROJECTS = 'projects'
TEAMS = 'teams'
TYPE = 'type'
APPROVED_BY = 'approved_by'
REJECTED_BY = 'rejected_by'
STATUS = 'status'
OWNERS = 'owners'
IMPLEMENTERS = 'implementers'
DESIGNERS = 'designers'
TESTERS = 'testers'
OBSERVERS = 'observers'
SUPERVISORS = 'supervisors'
IMPORTANCE = 'importance'
URGENCY = 'urgency'
COMPLEXITY = 'complexity'
TAGS = 'tags'

fieldsData = {
    CREATED_BY: { 'dataType': users.valid, 'isList': False },
    CREATED_TIME: { 'dataType': None, 'isList': False },
    PROJECTS: { 'dataType': projects.valid, 'isList': True },
    TEAMS: { 'dataType': teams.valid, 'isList': True },
    TYPE: { 'dataType': tasks.types, 'isList': False },
    APPROVED_BY: { 'dataType': users.valid, 'isList': True },
    REJECTED_BY: { 'dataType': users.valid, 'isList': True },
    STATUS: { 'dataType': tasks.status, 'isList': False },
    OWNERS: { 'dataType': users.valid, 'isList': True },
    IMPLEMENTERS: { 'dataType': users.valid, 'isList': True },
    DESIGNERS: { 'dataType': users.valid, 'isList': True },
    TESTERS: { 'dataType': users.valid, 'isList': True },
    OBSERVERS: { 'dataType': users.valid, 'isList': True },
    SUPERVISORS: { 'dataType': users.valid, 'isList': True },
    IMPORTANCE: { 'dataType': priority.valid, 'isList': False },
    URGENCY: { 'dataType': priority.valid, 'isList': False },
    COMPLEXITY: { 'dataType': complexity.valid, 'isList': False },
    TAGS: { 'dataType': None, 'isList': True }}

def dataType(field):
    return fieldsData[field]['dataType']

def isList(field):
    return fieldsData[field]['isList']

def isValid(field, value = None):
    return (field in fieldsData) and (value == None or dataType(field) == None or value in dataType(field) or (value.isdigit() and int(value) in dataType(field)))

def add(taskPath, field, value, replaceCurrentList = False):
    assert isinstance(taskPath, str)
    assert isValid(field, value)

    fieldPath = taskPath + os.sep + field
    if isList(field):    
        if not os.path.exists(fieldPath):
            os.makedirs(fieldPath)
        elif replaceCurrentList:
            for valueFile in os.listdir(fieldPath):
                os.remove(valueFile)
        filePtr = open(fieldPath + os.sep + str(value), 'w')
        filePtr.close()
        return

    remove(taskPath, field)
    filePtr = open(fieldPath + '-' + str(value), 'w')
    filePtr.close()

def remove(taskPath, field, valueToRemove = None):
    assert isinstance(taskPath, str)
    assert isValid(field)

    fieldPath = taskPath + os.sep + field
    if isList(field):
        assert os.path.exists(fieldPath)
        if not valueToRemove:
            shutil.rmtree(fieldPath)
            return
        valueFile = fieldPath + os.sep + str(valueToRemove)
        assert os.path.isfile(valueFile)
        os.remove(valueFile)
        try:
            os.rmdir(fieldPath)
        except:
            pass
        return

    currentValue = glob.glob(taskPath + os.sep + field + '-*')
    if not currentValue:
        return
    assert len(currentValue) == 1
    os.remove(currentValue[0])
