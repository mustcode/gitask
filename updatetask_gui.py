import tkinter as tk
import os
import subprocess

from action import Action
import settings

class UpdateTaskPanel(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.populateData()
        self.populateActions()
        master.bind('<Return>', self.updateTaskKey)

    def createWidgets(self):
        self.taskListbox = tk.Listbox(self, width = 100, exportselection = False)
        self.taskListbox.pack()
        self.taskListbox.focus_set()
        self.actionListbox = tk.Listbox(self, width = 100, exportselection = False)
        self.actionListbox.pack()
        self.updateButton = tk.Button(self, text = "Update Task", command = self.updateTask)
        self.updateButton.pack()
        self.refreshButton = tk.Button(self, text = "Refresh", command = self.populateData)
        self.refreshButton.pack()
        self.syncButton = tk.Button(self, text = "Sync", command = self.syncData)
        self.syncButton.pack()

    def populateActions(self):
        index = 1
        for action in Action:
            self.actionListbox.insert(index, action.name)
            index += 1

    def populateData(self):
        self.clearData();
        if not os.path.exists(settings.TASKS_DIR):
            return
        index = 1
        for task in os.listdir(settings.TASKS_DIR):
            taskPath = settings.TASKS_DIR + os.sep + task
            self.taskListbox.insert(index, taskPath)
            index += 1

    def clearData(self):
        itemCount = self.taskListbox.size()
        self.taskListbox.delete(0, itemCount-1)

    def updateTask(self):
        task = self.taskListbox.get(self.taskListbox.curselection()[0])
        action = self.actionListbox.get(self.actionListbox.curselection()[0])
        subprocess.call([settings.PYTHON_EXE, 'updatetask.py', task, action])

    def updateTaskKey(self, event):
        self.updateTask()

    def syncData(sefl):
        subprocess.call([settings.PYTHON_EXE, 'sync.py'])

root = tk.Tk()
root.title("Gitask - update task")
app = UpdateTaskPanel(master=root)
app.mainloop()