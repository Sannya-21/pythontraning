# Contact Book using Dictionary

contacts = {
    "Rahul": "9876543210",
    "Priya": "9876543211",
    "Aman": "9876543212"
}

# Add Contact
contacts["Neha"] = "9876543213"
print("After Adding Contact:")
print(contacts)

# Search Contact
name = "Priya"
if name in contacts:
    print("\nContact Found:")
    print(name, ":", contacts[name])
else:
    print("\nContact Not Found")

# Update Contact
contacts["Aman"] = "9999999999"
print("\nAfter Updating Aman:")
print(contacts)

# Delete Contact
del contacts["Rahul"]
print("\nAfter Deleting Rahul:")
print(contacts)


# Detect Two-Digit Numbers using Set

numbers = {5, 12, 45, 100, 8, 67, 23, 456}

two_digit = set()

for num in numbers:
    if 10 <= num <= 99:
        two_digit.add(num)

print("\nOriginal Set:", numbers)
print("Two-Digit Numbers:", two_digit)