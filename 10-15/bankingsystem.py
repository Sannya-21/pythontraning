class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        with open("transactions.txt", "a") as file:
            file.write(
                f"Account {self.acc_no}: Deposited {amount}\n"
            )

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient Balance!"
            )

        self.balance -= amount

        with open("transactions.txt", "a") as file:
            file.write(
                f"Account {self.acc_no}: Withdrawn {amount}\n"
            )

    def check_balance(self):
        return self.balance


# Account numbers stored in list
account_numbers = [1001, 1002]

# Customer accounts stored in dictionary
customers = {
    1001: {"name": "Ali", "balance": 5000},
    1002: {"name": "Sara", "balance": 10000}
}

accounts = {}

for acc_no in account_numbers:
    accounts[acc_no] = BankAccount(
        acc_no,
        customers[acc_no]["name"],
        customers[acc_no]["balance"]
    )

try:
    accounts[1001].deposit(2000)
    accounts[1001].withdraw(1000)

    print("Account Number:", accounts[1001].acc_no)
    print("Customer Name :", accounts[1001].name)
    print("Balance       :", accounts[1001].check_balance())

except InsufficientBalanceError as e:
    print("Error:", e)