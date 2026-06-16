num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)



 def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is", factorial(num))