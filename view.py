import os
import shutil
from enum import Enum

import settings
import fields

def show(fromProjects, sortField, flat):
    assert isinstance(fromProjects, list)
    assert fields.isValid(sortField)

    if not os.path.exists(settings.TASKS_DIR):
        print('error: task folder not found.')
        return

    viewPath = settings.VIEWS_DIR + os.sep + '_'.join(fromProjects) + '-' + sortField.name
    
    if os.path.exists(viewPath):
        shutil.rmtree(viewPath)
    os.makedirs(viewPath)

    if not flat:
        dataType = fields.dataType(sortField)
        if dataType != None:
            for value in dataType:
                if isinstance(value, Enum):
                    value = value.name
                os.makedirs(viewPath + os.sep + str(value))

    print('processing tasks...')
    for task in os.listdir(settings.TASKS_DIR):
        print(task)
        taskPath = settings.TASKS_DIR + os.sep + task

        if fromProjects:
            projectsPath = taskPath + os.sep + fields.Field.projects.name
            if os.path.exists(projectsPath):
                projectsAssigned = os.listdir(projectsPath)
            else:
                projectsAssigned = []
            if not list(set(fromProjects) & set(projectsAssigned)):
                continue

        for field in os.listdir(taskPath):
            if not field.startswith(sortField.name):
                continue
            keyValue = field.split('-')
            key = keyValue[0]
            value = '-'.join(keyValue[1:])
            if flat:
                taskFile = open(viewPath + os.sep + value + '-' + task, 'w')
            else:
                valuePath = viewPath + os.sep + value
                if not os.path.exists(valuePath):
                    os.makedirs(valuePath)
                taskFile = open(valuePath + os.sep + task, 'w')
            taskFile.close()
    return
