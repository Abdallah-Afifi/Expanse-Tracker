import os
import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def display_expenses(self):
        print("\nYour Expenses:")
        if self.expenses:
            for expense in self.expenses:
                print(f"{expense['date']} - {expense['category']}: ${expense['amount']:.2f}")
        else:
            print("No expenses recorded.")

    def add_expense(self, category, amount):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_expense = {'date': date, 'category': category, 'amount': amount}
        self.expenses.append(new_expense)
        self.save_expenses()
        print("Expense recorded successfully.")

    def calculate_total_expenses(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total_expenses:.2f}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nOptions:")
        print("1. Display Expenses")
        print("2. Add Expense")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            expense_tracker.display_expenses()
        elif choice == '2':
            category = input("Enter the category of the expense: ")
            amount = float(input("Enter the amount of the expense: "))
            expense_tracker.add_expense(category, amount)
        elif choice == '3':
            expense_tracker.calculate_total_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
