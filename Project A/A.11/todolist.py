"""
Add Task: Allow users to add a new task to the to-do list.
View Tasks: Display the list of tasks.
Edit Task: Allow users to edit an existing task.
Delete Task: Allow users to delete a task.
Save Tasks to File: Save the list of tasks to a file.
Load Tasks from File: Load the list of tasks from a file.


Entry: A single-line text entry field.
Text: A multi-line text entry field.
Listbox: A list of items.
Checkbutton: A checkbox that can be toggled on or off.
Radiobutton: A radio button that allows the user to select one option from a set.
Scale: A slider that allows the user to select a value from a range.
Spinbox: A text entry field with up and down arrows to select from a range of values.
Combobox: A drop-down list of options (requires ttk module).
Frame: A container widget to group other widgets.
Canvas: A widget for drawing shapes, images, and other complex layouts.
Menu: A menu bar for creating drop-down menus.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
class ToDo:
    def __init__(self, root):
        self.tasks = []
        
        self.root = root
        root.title("To-do-list")

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.7)
        root.geometry(f"{window_width}x{window_height}")

        # Header sizes
        Header1 = int(window_height * 0.05)
        Header2 = int(window_height * 0.03)
        Header3 = int(window_height * 0.02)

        margin1 = int(window_width * 0.1)
        margin2 = int(window_width * 0.08)

        # Title
        self.header_title = Label(root, text="Welcome to To-do-list", font=('Tekton Pro', Header1))
        self.header_title.pack(side=TOP, fill=X, padx=10, pady=10)

        # Button Frames
        self.bottom_frame = Frame(root, bd=5, bg='light grey')
        self.bottom_frame.pack(side=BOTTOM, padx=margin1, pady=10, fill=X)

        # Buttons
        self.add_task_btn = Button(self.bottom_frame, text="Add Task", bd=3, command=self.add_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.add_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.view_task_btn = Button(self.bottom_frame, text="View Tasks", bd=3, command=self.view_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.view_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.edit_task_btn = Button(self.bottom_frame, text="Edit Tasks", bd=3, command=self.edit_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.edit_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)
        
        self.delete_task_btn = Button(self.bottom_frame, text="Delete Tasks", bd=3, command=self.delete_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.delete_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.save_task_btn = Button(self.bottom_frame, text="Save Tasks", bd=3, command=self.save_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.save_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.load_task_btn = Button(self.bottom_frame, text="Load Tasks", bd=3, command=self.load_task, font=('Arial', Header3), relief='groove', cursor='hand2')
        self.load_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        # Add Task Frame
        self.add_frame = Frame(root, bd=5, bg='yellow')
        

        self.label_task1 = Label(self.add_frame, font=('Times New Roman', Header3), text="Enter Task: ")
        self.label_task1.pack(padx=(margin2,0), pady=10, side=LEFT)

        self.entry_task = Entry(self.add_frame, font=('Arial', Header3), width=50)
        self.entry_task.pack(pady=10, side=LEFT)

        # View Task Frame
        self.view_frame = Frame(root, bd=5, bg='green')

        # Edit Task Frame
        self.edit_frame = Frame(root, bd=5, bg='orange')

        # Delete Task Frame
        self.delete_frame = Frame(root, bd=5, bg='purple')

        # Save Task Frame
        self.save_frame = Frame(root, bd=5, bg='red')
        
        # Load Task Frame
        self.load_frame = Frame(root, bd=5, bg='blue')

    def add_task(self):
        self.view_frame.pack_forget()
        self.edit_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack_forget()
        self.add_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

    def view_task(self):
        self.add_frame.pack_forget()
        self.edit_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack_forget()
        self.view_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

    def edit_task(self):
        self.add_frame.pack_forget()
        self.view_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack_forget()
        self.edit_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

    def delete_task(self):
        self.add_frame.pack_forget()
        self.view_frame.pack_forget()
        self.edit_frame.pack_forget()
        self.save_frame.pack_forget()
        self.delete_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

    def save_task(self):
        self.add_frame.pack_forget()
        self.view_frame.pack_forget()
        self.edit_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

    def load_task(self):
        self.add_frame.pack_forget()
        self.view_frame.pack_forget()
        self.edit_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack_forget()

    def main(self):
        pass

if __name__ == "__main__":
    root = Tk()
    do = ToDo(root)
    root.mainloop()