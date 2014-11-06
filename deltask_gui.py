import tkinter as tk
import os
import subprocess

import settings

class DeleteTaskPanel(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.populateData()
        master.bind('<Return>', self.deleteTaskKey)

    def createWidgets(self):
        self.taskListbox = tk.Listbox(self, width = 100)
        self.taskListbox.pack()
        self.taskListbox.focus_set()
        self.deleteButton = tk.Button(self, text = "Delete Task", command = self.deleteTask)
        self.deleteButton.pack()
        self.refreshButton = tk.Button(self, text = "Refresh", command = self.populateData)
        self.refreshButton.pack()
        self.syncButton = tk.Button(self, text = "Sync", command = self.syncData)
        self.syncButton.pack()

    def populateData(self):
        self.clearData();
        index = 1
        for task in os.listdir(settings.TASKS_DIR):
            print(task)
            taskPath = settings.TASKS_DIR + os.sep + task
            self.taskListbox.insert(index, taskPath)
            index += 1

    def clearData(self):
        itemCount = self.taskListbox.size()
        self.taskListbox.delete(0, itemCount-1)

    def deleteTask(self):
        selection = self.taskListbox.get(self.taskListbox.curselection()[0])
        subprocess.call([settings.PYTHON_EXE, 'deltask.py', selection])
        self.populateData();

    def deleteTaskKey(self, event):
        self.deleteTask()

    def syncData(sefl):
        subprocess.call([settings.PYTHON_EXE, 'sync.py'])

root = tk.Tk()
root.title("Gitask - delete task")
app = DeleteTaskPanel(master=root)
app.mainloop()