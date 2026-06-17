import csv

FILENAME = "library_books.csv"

# Function to add a book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author])

    print("Book added successfully!\n")


# Function to display all books
def display_books():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- Library Books ---")
            found = False

            for row in reader:
                found = True
                print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")

            if not found:
                print("No books available.")

    except FileNotFoundError:
        print("Error: Book file not found.\n")


# Function to search a book
def search_book():
    search_title = input("Enter book title to search: ")

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            found = False

            for row in reader:
                if row[1].lower() == search_title.lower():
                    print("\nBook Found:")
                    print(f"ID: {row[0]}")
                    print(f"Title: {row[1]}")
                    print(f"Author: {row[2]}")
                    found = True
                    break

            if not found:
                print("Book not found.")

    except FileNotFoundError:
        print("Error: Book file not found.\n")


# Function to remove a book
def remove_book():
    remove_id = input("Enter Book ID to remove: ")

    try:
        books = []

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            found = False

            for row in reader:
                if row[0] != remove_id:
                    books.append(row)
                else:
                    found = True

        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)

        if found:
            print("Book removed successfully!")
        else:
            print("Book ID not found.")

    except FileNotFoundError:
        print("Error: Book file not found.\n")


# Main Menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        display_books()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")