import os
import sys
import shutil

import settings
import fields

def show(projectFilters, sortByField):
    assert isinstance(projectFilters, list)
    assert isinstance(sortByField, str)

    viewPath = settings.VIEWS_DIR + os.sep + '_'.join(projectFilters) + '-' + sortByField
    
    if os.path.exists(viewPath):
        shutil.rmtree(viewPath)
    os.makedirs(viewPath)

    dataType = fields.dataType(sortByField)
    if dataType != None:
        for value in dataType:
            os.makedirs(viewPath + os.sep + value)

    print('processing tasks:')
    for task in os.listdir(settings.TASKS_DIR):
        print(task)
        taskPath = settings.TASKS_DIR + os.sep + task

        if projectFilters:
            projectsPath = taskPath + os.sep + fields.PROJECTS
            if os.path.exists(projectsPath):
                projectsAssigned = os.listdir(projectsPath)
            else:
                projectsAssigned = []
            if not list(set(projectFilters) & set(projectsAssigned)):
                continue

        for field in os.listdir(taskPath):
            if not field.startswith(sortByField):
                continue
            keyValue = field.split('-')
            key = keyValue[0]
            value = '-'.join(keyValue[1:])
            valuePath = viewPath + os.sep + value
            if not os.path.exists(valuePath):
                os.makedirs(valuePath)
            taskFile = open(valuePath + os.sep + task, 'w')
            taskFile.close()
    return
