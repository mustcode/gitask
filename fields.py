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

class Field(Enum):
    created_by = 1
    created_time = 2
    projects = 3
    teams = 4
    task_type = 5
    approved_by = 6
    rejected_by = 7
    status = 8
    owners = 9
    implementers = 10
    designers = 11
    testers = 12
    observers = 13
    supervisors = 14
    importance = 15
    urgency = 16
    complexity = 17
    tags = 18

fieldsData = {
    Field.created_by: { 'dataType': users.valid, 'isList': False },
    Field.created_time: { 'dataType': None, 'isList': False },
    Field.projects: { 'dataType': projects.valid, 'isList': True },
    Field.teams: { 'dataType': teams.valid, 'isList': True },
    Field.task_type: { 'dataType': tasks.Type, 'isList': False },
    Field.approved_by: { 'dataType': users.valid, 'isList': True },
    Field.rejected_by: { 'dataType': users.valid, 'isList': True },
    Field.status: { 'dataType': tasks.Status, 'isList': False },
    Field.owners: { 'dataType': users.valid, 'isList': True },
    Field.implementers: { 'dataType': users.valid, 'isList': True },
    Field.designers: { 'dataType': users.valid, 'isList': True },
    Field.testers: { 'dataType': users.valid, 'isList': True },
    Field.observers: { 'dataType': users.valid, 'isList': True },
    Field.supervisors: { 'dataType': users.valid, 'isList': True },
    Field.importance: { 'dataType': priority.valid, 'isList': False },
    Field.urgency: { 'dataType': priority.valid, 'isList': False },
    Field.complexity: { 'dataType': complexity.valid, 'isList': False },
    Field.tags: { 'dataType': None, 'isList': True }}

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
