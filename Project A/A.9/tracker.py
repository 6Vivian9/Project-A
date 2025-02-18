import json

class Tracker:
    def __init__(self):
        self.expenses = []
        self.description = str
        self.amount = float
        self.category = str

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

    def view_by_category(self):
        category = input("Enter Category: ")
        if not self.expenses:
            print("No Expenses Recorded yet")
            return
        else:
            for i in range (0, len(self.expenses)):
                if self.expenses[i][2] == category:
                    print(f"Description: {self.expenses[i][0]} Amount: {self.expenses[i][1]} Category: {self.expenses[i][2]}")
    
    def view_total(self):
        sum = float(0)
        if not self.expenses:
            print("No Expense Yet Recorded")
            return
        else:
            for i in range (0, len(self.expenses)):
                sum += self.expenses[i][1]
            print(f"Total: {sum:.2f}")
    
    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump([{"description": exp[0], "amount": exp[1], "category": exp[2]} for exp in self.expenses], file)
        print(f"Expenses saved to {filename}")

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                expenses_data = json.load(file)
                self.expenses = [(exp["description"], exp["amount"], exp["category"]) for exp in expenses_data]
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"No file found with name {filename}")


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
                track.view_by_category()
            elif choice == "4":
                track.view_total()
            elif choice == "5":
                filename = input("Enter File Name: ")
                track.save_expenses(filename)
            elif choice == "6":
                filename = input("Enter File Name: ")
                track.load_expenses(filename)
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