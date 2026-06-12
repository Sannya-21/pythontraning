balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Current Balance =", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Updated Balance =", balance)

elif choice == 3:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")