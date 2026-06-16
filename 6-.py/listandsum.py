# Create a list of 10 integers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Find the sum without using sum() function
total = 0

for num in numbers:
    total += num

print("List:", numbers)
print("Sum of all elements:", total)