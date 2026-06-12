# Contact Book

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact Added Successfully")

    elif choice == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact Updated Successfully")
        else:
            print("Contact Not Found")

    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")

    elif choice == 5:
        print("\nContacts List")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == 6:
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice")