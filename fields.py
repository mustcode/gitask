import sys
import os
import glob
import shutil
from enum import Enum

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
    importance = 9
    urgency = 10
    complexity = 11
    tags = 12

fieldsData = {
    Field.created_by: { 'dataType': users.valid, 'isList': False },
    Field.created_time: { 'dataType': None, 'isList': False },
    Field.projects: { 'dataType': projects.valid, 'isList': True },
    Field.teams: { 'dataType': teams.valid, 'isList': True },
    Field.task_type: { 'dataType': tasks.Type, 'isList': False },
    Field.approved_by: { 'dataType': users.valid, 'isList': True },
    Field.rejected_by: { 'dataType': users.valid, 'isList': True },
    Field.status: { 'dataType': tasks.Status, 'isList': False },
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

    if isinstance(value, Enum):
        value = value.name
    fieldPath = taskPath + os.sep + field.name
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

def remove(taskPath, field, value = None):
    assert isinstance(taskPath, str)
    assert isValid(field)

    fieldPath = taskPath + os.sep + field.name
    if isList(field):
        assert os.path.exists(fieldPath)
        if not value:
            shutil.rmtree(fieldPath)
            return
        if isinstance(value, Enum):
            value = value.name
        valueFile = fieldPath + os.sep + str(value)
        assert os.path.isfile(valueFile)
        os.remove(valueFile)
        try:
            os.rmdir(fieldPath)
        except:
            pass
        return

    currentValue = glob.glob(taskPath + os.sep + field.name + '-*')
    if not currentValue:
        return
    assert len(currentValue) == 1
    os.remove(currentValue[0])
