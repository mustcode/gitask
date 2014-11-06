import tkinter as tk
import subprocess

import settings

class AddTaskPanel(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        master.bind('<Return>', self.addTaskKey)

    def createWidgets(self):
        self.taskNameEntry = tk.Entry(self, width = 100)
        self.taskNameEntry.pack()
        self.taskNameEntry.focus_set()
        self.addButton = tk.Button(self, text = "Add Task", command = self.addTask)
        self.addButton.pack()
        self.syncButton = tk.Button(self, text = "Sync", command = self.syncData)
        self.syncButton.pack()

    def addTask(self):
        subprocess.call([settings.PYTHON_EXE, 'addtask.py', self.taskNameEntry.get()])
        self.taskNameEntry.delete(0, tk.END)
        self.taskNameEntry.focus_set()

    def addTaskKey(self, event):
        self.addTask()

    def syncData(sefl):
        subprocess.call([settings.PYTHON_EXE, 'sync.py'])

root = tk.Tk()
root.title("Gitask - add task")
app = AddTaskPanel(master=root)
app.mainloop()