# Student Result Management System

students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
marks_list = list(students.values())

average = sum(marks_list) / len(marks_list)
print("\nAverage Marks =", average)
#topper
topper = max(students, key=students.get)
print("Topper =", topper)
print("Topper Marks =", students[topper])

# Display grades
print("\nStudent Results")

for name, marks in students.items():

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "F"

    print(name, ":", marks, "Grade =", grade)