"""
Add Task: Allow users to add a new task to the to-do list.
View Tasks: Display the list of tasks.
Edit Task: Allow users to edit an existing task.
Delete Task: Allow users to delete a task.
Save Tasks to File: Save the list of tasks to a file.
Load Tasks from File: Load the list of tasks from a file.
"""

import tkinter as tk
from tkinter import *
import json

class todo:
    def __init__(self,root):
        self.root = root
        root.title("My First Tkinter App")
        root.geometry("400x300")

        self.label = Label(root, text="Hello Guys!", font=('Times New Roman', 18))
        self.label.pack(padx=10, pady=10)

        self.button = Button(root, text="Click!", command=self.on_button_click)
        self.button.pack(pady=10)



    def on_button_click(self):
        print("")

    def main(self):
        pass

if __name__ == "__main__":
    root = Tk()
    do = todo(root)
    root.mainloop()
