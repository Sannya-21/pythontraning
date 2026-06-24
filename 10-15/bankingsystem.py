class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Updated Balance = ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance!")

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Updated Balance = ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance = ₹{self.balance}")


# Account numbers stored in list
account_numbers = [1001, 1002, 1003]

# Customer details stored in dictionary
customers = {
    1001: {"name": "Ali", "balance": 5000},
    1002: {"name": "Sara", "balance": 8000},
    1003: {"name": "Ahmed", "balance": 12000},
    1004:{ "name": " sannya","balance": 10500000},
    1005:{" name":" jasmeen", "balance": 100056000}
}

# Create account objects
accounts = {}

for acc_no in account_numbers:
    accounts[acc_no] = BankAccount(
        acc_no,
        customers[acc_no]["name"],
        customers[acc_no]["balance"]
    )

# Ask Account ID
acc_id = int(input("Enter Account ID: "))

if acc_id not in accounts:
    print("Invalid Account ID!")

else:
    acc = accounts[acc_id]

    print(f"\nWelcome {acc.name}")

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
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

        except InsufficientBalanceError as e:
            print("Error:", e)