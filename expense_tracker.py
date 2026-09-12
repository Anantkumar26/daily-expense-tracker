expenses = []


def add_expense():
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")

    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['category']} - "
            f"{expense['description']} - ₹{expense['amount']:.2f}"
        )


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expense: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n===== Daily Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Daily Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
