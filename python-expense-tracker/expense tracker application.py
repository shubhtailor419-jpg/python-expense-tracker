class ExpenseTracker:
    """Manages personal expenses."""

    def __init__(self):
        self.expenses = []

    def add_expense(self):
        """Add a new expense."""
        try:
            description = input("Enter description: ").strip()
            if not description:
                description = "Miscellaneous"

            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            self.expenses.append({"description": description, "amount": amount})
            print("Expense added successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n--- Expense List ---")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense['description']}: Rs {expense['amount']:.2f}")

    def view_summary(self):
        """Display expense summary."""
        if not self.expenses:
            print("No expenses recorded.")
            return

        total = sum(expense["amount"] for expense in self.expenses)
        print("\n--- Expense Summary ---")
        print(f"Total Expenses: {len(self.expenses)}")
        print(f"Total Amount: Rs {total:.2f}")

    def delete_expense(self):
        """Delete an expense."""
        if not self.expenses:
            print("No expenses to delete.")
            return

        self.view_expenses()

        try:
            index = int(input("\nEnter expense number to delete: ")) - 1

            if 0 <= index < len(self.expenses):
                removed = self.expenses.pop(index)
                print(f"Deleted: {removed['description']} - Rs {removed['amount']:.2f}")
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Invalid input.")

    def display_menu(self):
        """Display menu options."""
        print("\n" + "=" * 30)
        print("EXPENSE TRACKER")
        print("=" * 30)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Delete Expense")
        print("5. Exit")
        print("=" * 30)

    def run(self):
        """Main application loop."""
        while True:
            self.display_menu()
            choice = input("Enter choice (1-5): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_summary()
            elif choice == "4":
                self.delete_expense()
            elif choice == "5":
                print("Thank you for using Expense Tracker.")
                break
            else:
                print("Invalid choice. Please select 1-5.")


def main():
    tracker = ExpenseTracker()
    tracker.run()


if __name__ == "__main__":
    main()


def main():
    """Entry point for the application."""
    tracker = ExpenseTracker()
    tracker.run()


if __name__ == "__main__":
    main()