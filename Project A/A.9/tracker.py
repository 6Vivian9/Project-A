"""
/ Add a new expense.
View all expenses.
View expenses by category.
View total expenses.
Save expenses to a file.
Load expenses from a file.

Add Expense: Allow users to add a new expense with a description, amount, and category.
View All Expenses: Display all recorded expenses.
View Expenses by Category: Filter and display expenses by a specific category.
View Total Expenses: Calculate and display the total amount of all expenses.
Save Expenses to File: Save the list of expenses to a JSON file.
Load Expenses from File: Load expenses from a JSON file.
"""

import json

class Tracker:
    def __init__(self):
        self.expenses = []
        self.description = str
        self.amount = float
        self.category = str

        self.description = "Cooking Oil"
        self.amount = 1.20
        self.category = "Cooking"
        expen = (self.description, self.amount, self.category)
        self.expenses.append(expen)
        self.description = "Bracelet"
        self.amount = 100.15
        self.category = "Accessory"
        expen = (self.description, self.amount, self.category)
        self.expenses.append(expen)

    def test(self):
        pass

    def add_expense(self):
        self.description = input("Enter Description: ")
        self.amount = float(input("Enter Amount: "))
        self.category = input("Enter Category: ")
        expen = (self.description, self.amount, self.category)
        self.expenses.append(expen)

    def view_all_expenses(self):
        if not self.expenses:
            print("No Expenses Recorded")
            return
        else:
            for i in range(0, len(self.expenses)):
                print(f"Description: {self.expenses[i][0]} Amount: {self.expenses[i][1]} Category: {self.expenses[i][2]}")

    def ui(self):
        while True:
            print(f"\nExpense Tracker Main Menu:"
                f"\n[1]. Add Expense"
                f"\n[2]. View All Expenses"
                f"\n[3]. View Expenses by Category"
                f"\n[4]. View Total Expenses"
                f"\n[5]. Save Expenses to File"
                f"\n[6]. Load Expenses from File"
                f"\n[7]. Exit")
            choice = input("Enter Choice: ")

            if choice == "1":
                track.add_expense()
            elif choice == "2":
                track.view_all_expenses()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                pass
                break
            else:
                print("Invalid Input:")

    def main(self):
        pass
        track.ui()

    


if __name__ == "__main__":
    track = Tracker()
    track.main()