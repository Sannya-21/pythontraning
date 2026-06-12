# Shopping Cart System

items = []

n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter item name: ")
    items.append(item)

print("Items in Cart:", items)

remove_item = input("Enter item to remove: ")

if remove_item in items:
    items.remove(remove_item)

print("Updated Cart:", items)

# Categories using Set
categories = set()

for item in items:
    category = input(f"Enter category for {item}: ")
    categories.add(category)

print("Unique Categories:", categories)

# Prices using Dictionary
prices = {}

for item in items:
    price = float(input(f"Enter price of {item}: "))
    prices[item] = price

print("Item Prices:", prices)

# Total Bill
total_bill = sum(prices.values())

print("Total Bill =", total_bill)