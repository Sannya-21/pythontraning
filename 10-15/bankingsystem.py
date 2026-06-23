class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        print(f"\n₹{amount} deposited successfully.")
        print(f"Updated Balance = ₹{self.balance}")

        with open("transactions.txt", "a") as file:
            file.write(f"Deposited ₹{amount}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient Balance!"
            )

        self.balance -= amount

        print(f"\n₹{amount} withdrawn successfully.")
        print(f"Updated Balance = ₹{self.balance}")

        with open("transactions.txt", "a") as file:
            file.write(f"Withdrawn ₹{amount}\n")

    def check_balance(self):
        print(f"\nCurrent Balance = ₹{self.balance}")


# Account numbers stored in list
account_numbers = [1001]

# Customer details stored in dictionary
customers = {
    1001: {
        "name": "Ali",
        "balance": 5000
    }
}

# Create Account Object
acc = BankAccount(
    1001,
    customers[1001]["name"],
    customers[1001]["balance"]
)

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    try:
        if choice == 1:
            amount = float(input("Enter Deposit Amount: "))
            acc.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter Withdrawal Amount: "))
            acc.withdraw(amount)

        elif choice == 3:
            acc.check_balance()

        elif choice == 4:
            print("Thank You for Using Banking System")
            break

        else:
            print("Invalid Choice!")

    except InsufficientBalanceError as e:
        print("Error:", e)