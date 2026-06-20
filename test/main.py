from grade_module import calculate_grade

# Student details stored using tuples
students = [
    (101, "Rahul"),
    (102, "Priya"),
    (103, "Aman")
]

# Marks stored in dictionary
marks = {
    101: [85, 90, 80],
    102: [95, 88, 92],
    103: [70, 75, 72]
}

# List to maintain student records
student_records = []

# Process Results
for roll_no, name in students:

    total = sum(marks[roll_no])
    percentage = total / len(marks[roll_no])

    grade = calculate_grade(percentage)

    record = {
        "Roll No": roll_no,
        "Name": name,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    student_records.append(record)

# Store records in file
with open("results.txt", "w") as file:

    file.write("EXAM RESULT REPORT\n")
    file.write("-" * 50 + "\n")

    for student in student_records:
        file.write(
            f"{student['Roll No']} | "
            f"{student['Name']} | "
            f"Total: {student['Total']} | "
            f"Percentage: {student['Percentage']} | "
            f"Grade: {student['Grade']}\n"
        )

# Generate Rank List
rank_list = sorted(
    student_records,
    key=lambda x: x["Percentage"],
    reverse=True
)

print("\nRANK LIST")
print("-" * 50)

rank = 1
for student in rank_list:
    print(
        f"Rank {rank}: "
        f"{student['Name']} "
        f"({student['Percentage']}%)"
    )
    rank += 1

# Grade Report
print("\nGRADE REPORT")
print("-" * 50)

for student in student_records:
    print(
        f"{student['Name']} - "
        f"{student['Grade']}"
    )

print("\nResults saved in results.txt")