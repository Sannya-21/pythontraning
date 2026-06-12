import math

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")
print("10. Logarithm")
print("11. Factorial")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a + b)

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a - b)

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a * b)

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero is not allowed")

elif choice == 5:
    num = float(input("Enter a number: "))
    print("Square Root =", math.sqrt(num))

elif choice == 6:
    base = float(input("Enter base: "))
    exp = float(input("Enter exponent: "))
    print("Result =", math.pow(base, exp))

elif choice == 7:
    angle = float(input("Enter angle in degrees: "))
    print("Sine =", math.sin(math.radians(angle)))

elif choice == 8:
    angle = float(input("Enter angle in degrees: "))
    print("Cosine =", math.cos(math.radians(angle)))

elif choice == 9:
    angle = float(input("Enter angle in degrees: "))
    print("Tangent =", math.tan(math.radians(angle)))

elif choice == 10:
    num = float(input("Enter a number: "))
    print("Log =", math.log10(num))

elif choice == 11:
    num = int(input("Enter a number: "))
    print("Factorial =", math.factorial(num))

else:
    print("Invalid Choice")