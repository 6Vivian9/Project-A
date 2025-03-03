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
from tkcalendar import *
from datetime import datetime,time
import time as tm
import json
class ToDo:
    def __init__(self, root):
        self.tasks = [('O', '#02', '#03', '#04'),('O', '#12', '#13', '#14'),('O', '#22', '#23', '#24'),('O', '#32', '#33', '#34')]
        self.done = []

        current_time = tm.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        
        self.root = root
        root.title("To-do-list")

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.7)
        root.geometry(f"{window_width}x{window_height}")

        # Header sizes
        self.Header1 = int(window_height * 0.05)
        self.Header2 = int(window_height * 0.03)
        self.Header3 = int(window_height * 0.02)

        self.margin1 = int(window_width * 0.1)
        self.margin2 = int(window_width * 0.08)

        # Title
        self.header_title = Label(root, text="Welcome to To-do-list", font=('Tekton Pro', self.Header1))
        self.header_title.pack(side=TOP, fill=X, padx=10, pady=10)

        # Button Frames
        self.bottom_frame = Frame(root, bd=5, bg='light grey')
        self.bottom_frame.pack(side=BOTTOM, padx=self.margin1, pady=10, fill=X)

        # Buttons
        self.add_task_btn = Button(self.bottom_frame, text="Add Task", bd=3, command=self.add_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.add_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.view_task_btn = Button(self.bottom_frame, text="View Tasks", bd=3, command=self.view_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.view_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.edit_task_btn = Button(self.bottom_frame, text="Edit Tasks", bd=3, command=self.edit_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.edit_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)
        
        self.delete_task_btn = Button(self.bottom_frame, text="Delete Tasks", bd=3, command=self.delete_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.delete_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.save_task_btn = Button(self.bottom_frame, text="Save Tasks", bd=3, command=self.save_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.save_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        self.load_task_btn = Button(self.bottom_frame, text="Load Tasks", bd=3, command=self.load_task, font=('Arial', self.Header3), relief='groove', cursor='hand2')
        self.load_task_btn.pack(padx=10, pady=10, side=LEFT, expand=True)

        # Add Task Frame
        self.add_frame = Frame(root, bd=5)
        
        # Input Task Frame
        self.task_input_frame = Frame(self.add_frame, bd=5)
        self.task_input_frame.pack(padx=10, pady=(5,10), side=TOP, fill=X)

        self.label_task1 = Label(self.task_input_frame, font=('Times New Roman', self.Header3), text="Enter Task: ")
        self.label_task1.pack(padx=(self.margin2,0), pady=10, side=LEFT)

        self.entry_task = Entry(self.task_input_frame, font=('Arial', self.Header3), width=50)
        self.entry_task.pack(pady=10, side=LEFT)

        # Calendar Task Frame
        self.task_calendar_input = Frame(self.add_frame, bd=5)
        self.task_calendar_input.pack(padx=10, pady=0, side=TOP, fill=X)

        self.label_task2 = Label(self.task_calendar_input, font=('Times New Roman', self.Header3), text="Enter Date: ")
        self.label_task2.pack(padx=(self.margin2,0), pady=10, side=LEFT)

        self.cal = DateEntry(self.task_calendar_input ,width=15, background='white',foreground='black', borderwidth=2, year=2024, locale='en_US', date_pattern='yyyy-mm-dd')
        self.cal.pack(padx=5, pady=5, side=LEFT)

        # Time Task Frame
        self.task_time_input = Frame(self.add_frame, bd=5)
        self.task_time_input.pack(side=TOP, padx=10, pady=0, fill=X)

        self.label_task3 = Label(self.task_time_input, font=('Times New Roman', self.Header3), text="Enter Deadline: ")
        self.label_task3.pack(padx=(self.margin2,0), pady=10, side=LEFT)

        hours = [f"{i:02d}" for i in range(1,13)]
        hourrightnow = current_hour
        AMPM = str
        if current_time.tm_hour > 12:
            hourrightnow -= 12
            AMPM = "PM"
        else:
            AMPM = "AM"
        self.hour_combo = ttk.Combobox(self.task_time_input,values=hours,width=3,state='readonly')
        self.hour_combo.set(hourrightnow)
        self.hour_combo.pack(side=LEFT, padx=2)

        self.separator1 = Label(self.task_time_input, text=":", font=('Arial', self.Header3))
        self.separator1.pack(side=LEFT)

        minutes = [f"{i:02d}" for i in range(60)] 
        self.minute_combo = ttk.Combobox(self.task_time_input,values=minutes,width=3,state='readonly'
        )
        self.minute_combo.set(current_time.tm_min)
        self.minute_combo.pack(side=LEFT, padx=2)

        self.separator2 = Label(self.task_time_input, text=":", font=('Arial', self.Header3))
        self.separator2.pack(side=LEFT)

        self.AMPM_combo = ttk.Combobox(self.task_time_input,values=('AM','PM'),width=3,state='readonly'
        )
        self.AMPM_combo.set(AMPM)
        self.AMPM_combo.pack(side=LEFT, padx=2)


        self.task_submit1 = Button(self.add_frame, text='Submit', bd=5, relief='groove', command=self.task_add_submit, font=('bookman old style', self.Header3))
        self.task_submit1.pack(padx=10, pady=15, side=TOP)

        # View Task Frame
        self.view_frame = Frame(root, bd=5)
        self.refresh = Button(self.view_frame, text='Refresh', font=('Arial', self.Header3), relief='groove', bd=3, command=self.refresh_table)
        self.refresh.pack(padx=5, pady=5, side=BOTTOM)

        columns = ('Status', 'Task', 'Date', 'Time')
        self.view_tree = ttk.Treeview(self.view_frame, columns=columns, show='headings')

        self.view_tree.heading('Status', text='Status')
        self.view_tree.heading('Task', text='Task')
        self.view_tree.heading('Date', text='Date')
        self.view_tree.heading('Time', text='Time')

        self.view_tree.column('Status', width=10, anchor='center')
        self.view_tree.column('Task', width=300, anchor='center', stretch=True)
        self.view_tree.column('Date', width=100, anchor='center')
        self.view_tree.column('Time', width=100, anchor='center')

        scrollbar = ttk.Scrollbar(self.view_tree, orient=VERTICAL, command=self.view_tree.yview)
        self.view_tree.configure(yscrollcommand=scrollbar.set)

        self.view_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
        scrollbar.pack(side=RIGHT, fill=Y)



        # Edit Task Frame
        self.edit_frame = Frame(root, bd=5)

        self.button_frame_edit = Frame(self.edit_frame, bd=5)
        self.button_frame_edit.pack(fill=X, anchor='center', side=BOTTOM)

        self.saved_button = Button(self.button_frame_edit, text='Edit', font=('Arial', self.Header3), relief='groove', bd=3, command=self.edit_row)
        self.saved_button.pack(padx=5, pady=5, side=LEFT, expand=True)

        self.saved_button = Button(self.button_frame_edit, text='Save', font=('Arial', self.Header3), relief='groove', bd=3, command=self.save_edit)
        self.saved_button.pack(padx=5, pady=5, side=LEFT, expand=True)

        columns = ('Task', 'Date', 'Time')
        self.view_tree_edit = ttk.Treeview(self.edit_frame, columns=columns, show='headings')

        self.view_tree_edit.heading('Task', text='Task')
        self.view_tree_edit.heading('Date', text='Date')
        self.view_tree_edit.heading('Time', text='Time')

        self.view_tree_edit.column('Task', width=300, anchor='center', stretch=True)
        self.view_tree_edit.column('Date', width=100, anchor='center')
        self.view_tree_edit.column('Time', width=100, anchor='center')

        scrollbar = ttk.Scrollbar(self.view_tree_edit, orient=VERTICAL, command=self.view_tree_edit.yview)
        self.view_tree_edit.configure(yscrollcommand=scrollbar.set)

        self.view_tree_edit.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
        scrollbar.pack(side=RIGHT, fill=Y)




        
        # Delete Task Frame
        self.delete_frame = Frame(root, bd=5, bg='purple')

        # Save Task Frame
        self.save_frame = Frame(root, bd=5, bg='red')
        
        # Load Task Frame
        self.load_frame = Frame(root, bd=5, bg='blue')

        self.status_frame = Frame(self.view_frame, bg='red')
        self.status_frame.pack(fill=X)

    def save_edit(self):
        pass

    def edit_row(self):
        selected_item = self.view_tree_edit.selection()
        if selected_item:
            item_values = self.view_tree_edit.item(selected_item, 'values')
            print(f"{item_values}")



    def refresh_table(self):
        child = self.view_tree.get_children()
        self.deletes = []

        for i in range (0, len(self.tasks)):
            values = self.view_tree.item(child[i])['values']
            if values[0] == '✓':
                self.deletes.append(i)
                self.done.append(self.view_tree.item(child[i])['values'])


        self.deletes.reverse()
        for a in range (0,len(self.deletes)):
            del self.tasks[self.deletes[a]]

        self.deletes.clear

        for item in self.view_tree.get_children():
            self.view_tree.delete(item)

        for task in self.tasks:
            item = self.view_tree.insert('', END, values=('O', task[1], task[2], task[3]))

    def task_add_submit(self):
        task_text = self.entry_task.get()
        selected_date = self.cal.get_date()
        selected_hour = self.hour_combo.get()
        selected_min = self.minute_combo.get()
        select_AMPM = self.AMPM_combo.get()

        if select_AMPM == "PM":
            selected_hour = int(selected_hour) + 12

        if task_text == "":
            self.error = "Invalid No Task"
            self.error_label = Label(self.add_frame, font=('cambria', self.Header3), fg='red', text=f'{self.error}')
            self.error_label.pack(padx=10,pady=0,side=TOP)
        else:
            selected_time = (f"{selected_hour}:{selected_min}")
            task = ("O" ,task_text, selected_date, selected_time)
            self.tasks.append(task)

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
        self.view_frame.pack(expand=True,pady=0,padx=10, fill=BOTH)

        for item in self.view_tree.get_children():
            self.view_tree.delete(item)

        for task in self.tasks:
            item = self.view_tree.insert('', END, values=('O', task[1], task[2], task[3]))
            
        self.view_tree.bind('<Button-1>', self.toggle_checkbox)
        
    def toggle_checkbox(self, event):
        region = self.view_tree.identify_region(event.x, event.y)
        if region == "cell":
            column = self.view_tree.identify_column(event.x)
            if column == '#1':
                item = self.view_tree.identify_row(event.y)
                if item:
                    self.row_number = self.view_tree.index(item)
                    values = self.view_tree.item(item)['values']
                    new_status = '✓' if values[0] == 'O' else 'O'
                    values = list(values)
                    values[0] = new_status
                    self.view_tree.item(item, values=values)
                    

    def edit_task(self):
        self.add_frame.pack_forget()
        self.view_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.save_frame.pack_forget()
        self.edit_frame.pack(expand=True,pady=10,padx=10, fill=BOTH)

        for item in self.view_tree_edit.get_children():
            self.view_tree_edit.delete(item)

        for task in self.tasks:
            item = self.view_tree_edit.insert('', END, values=(task[1], task[2], task[3]))
            
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