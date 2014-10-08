import os
import re

def setPriority(taskPath, urgency, importance):
    assert isinstance(taskPath, str)
    assert isinstance(importance, int)
    assert isinstance(urgency, int)
    assert urgency >= 0 and urgency <= 9
    assert importance >= 0 and importance <= 9

    pathList = os.path.split(taskPath)
    taskDir = pathList[0]
    taskName = pathList[1]

    priorityPrefix = str(urgency) + str(importance) + '-'
    if hasPriority(taskName):
        taskName = priorityPrefix + taskName[3:]
    else:
        taskName = priorityPrefix + taskName
    os.rename(taskPath, taskDir + os.sep + taskName)

def hasPriority(taskName):
    assert isinstance(taskName, str)
    return len(taskName) > 3 and taskName[2] == '-' and taskName[:2].isdigit()
