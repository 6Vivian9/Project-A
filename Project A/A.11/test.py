import tkinter as tk
from tkinter import ttk

class CheckboxTreeview(ttk.Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create a checkbox column
        self['columns'] = ('checkbox', 'name')
        self.column('#0', width=0, stretch=tk.NO)  # Hide first column
        self.column('checkbox', width=50, anchor='center')
        self.column('name', width=150)
        
        # Create column headings
        self.heading('#0', text='')
        self.heading('checkbox', text='Select')
        self.heading('name', text='Name')
        
        # Dictionary to store checkbox states
        self.checkboxes = {}
        
        # Bind click event
        self.bind('<Button-1>', self.checkbox_click)
        
    def insert_row(self, index, name, checked=False):
        item = self.insert('', index, values=('✓' if checked else '☐', name))
        self.checkboxes[item] = checked
        
    def checkbox_click(self, event):
        # Get the item that was clicked
        item = self.identify_row(event.y)
        col = self.identify_column(event.x)
        
        # Check if checkbox column was clicked
        if col == '#1' and item:
            # Toggle checkbox state
            checked = not self.checkboxes.get(item, False)
            self.checkboxes[item] = checked
            self.set(item, 'checkbox', '✓' if checked else '☐')

# Example usage
root = tk.Tk()
root.title("Checkbox Treeview")

tree = CheckboxTreeview(root)
tree.pack(padx=10, pady=10)

# Add some sample rows
tree.insert_row(0, "Item 1", checked=True)
tree.insert_row(1, "Item 2")
tree.insert_row(2, "Item 3", checked=True)

root.mainloop()