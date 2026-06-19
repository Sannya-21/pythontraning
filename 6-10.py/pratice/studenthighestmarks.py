students = {
    "Jasmeen": 85,
    "Aman": 92,
    "Simran": 88,
    "Rohan": 95
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Marks:", students[highest_student])