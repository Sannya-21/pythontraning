# File Handling in Python - All Modes

filename = "student.txt"

# -----------------------------
# 1. Write Mode (w)
# Creates a new file or overwrites existing content
# -----------------------------
with open(filename, "w") as file:
    file.write("Jasmeen - 85\n")
    file.write("Aman - 92\n")
    file.write("Simran - 88\n")

print("Data written using 'w' mode.")

# -----------------------------
# 2. Read Mode (r)
# Reads file content
# -----------------------------
with open(filename, "r") as file:
    print("\nContent using 'r' mode:")
    print(file.read())

# -----------------------------
# 3. Append Mode (a)
# Adds data at the end of file
# -----------------------------
with open(filename, "a") as file:
    file.write("Rohan - 95\n")

print("Data appended using 'a' mode.")

# -----------------------------
# 4. Read and Write Mode (r+)
# Reads and writes without deleting content
# -----------------------------
with open(filename, "r+") as file:
    print("\nContent using 'r+' mode:")
    print(file.read())

    file.write("Priya - 90\n")

print("Data added using 'r+' mode.")

# -----------------------------
# 5. Write and Read Mode (w+)
# Deletes old content, writes new content,
# and allows reading
# -----------------------------
with open(filename, "w+") as file:
    file.write("New Record\n")
    file.write("Karan - 80\n")

    file.seek(0)   # Move cursor to beginning

    print("\nContent using 'w+' mode:")
    print(file.read())

# -----------------------------
# 6. Append and Read Mode (a+)
# Appends data and allows reading
# -----------------------------
with open(filename, "a+") as file:
    file.write("Mehak - 87\n")

    file.seek(0)

    print("\nContent using 'a+' mode:")
    print(file.read())

# -----------------------------
# Additional Methods
# -----------------------------
with open(filename, "r") as file:
    print("First Line:")
    print(file.readline())

with open(filename, "r") as file:
    print("\nAll Lines:")
    lines = file.readlines()
    print(lines)

print("\nFile handling completed successfully.")