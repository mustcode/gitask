import os
import sys
import shutil

import settings
import fields

def show(fromProjects, sortField):
    assert isinstance(fromProjects, list)
    assert isinstance(sortField, str)

    viewPath = settings.VIEWS_DIR + os.sep + '_'.join(fromProjects) + '-' + sortField
    
    if os.path.exists(viewPath):
        shutil.rmtree(viewPath)
    os.makedirs(viewPath)

    dataType = fields.dataType(sortField)
    if dataType != None:
        for value in dataType:
            os.makedirs(viewPath + os.sep + value)

    print('processing tasks...')
    for task in os.listdir(settings.TASKS_DIR):
        print(task)
        taskPath = settings.TASKS_DIR + os.sep + task

        if fromProjects:
            projectsPath = taskPath + os.sep + fields.PROJECTS
            if os.path.exists(projectsPath):
                projectsAssigned = os.listdir(projectsPath)
            else:
                projectsAssigned = []
            if not list(set(fromProjects) & set(projectsAssigned)):
                continue

        for field in os.listdir(taskPath):
            if not field.startswith(sortField):
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

if len(sys.argv) < 3:
    print('error: expected at least 2 arguments')
    print('usage: view <projects...> <sort-field>')
    sys.exit()

fromProjects = sys.argv[1:-1]
sortField = sys.argv[-1]
print("from projects: " + str(fromProjects))
print("sort field: " + sortField)
show(fromProjects, sortField)
