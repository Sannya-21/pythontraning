# Expense Tracker

FILE_NAME = "expenses.txt"


def add_expense():
    """Add an expense to the file."""
    try:
        category = input("Enter category (Food, Travel, Shopping, etc.): ").strip()

        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense added successfully!")

    except ValueError as e:
        print("Invalid input:", e)


def summarize_expenses():
    """Read expenses and display summary by category."""
    expenses = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                amount = float(amount)

                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount

        print("\nExpense Summary by Category")
        print("-" * 30)

        total = 0
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount:.2f}")
            total += amount

        print("-" * 30)
        print(f"Total Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expense file found. Add some expenses first.")

    except Exception as e:
        print("Error reading file:", e)


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                summarize_expenses()

            elif choice == 3:
                print("Goodbye!")
                break

            else:
                print("Please enter a valid option (1-3).")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":