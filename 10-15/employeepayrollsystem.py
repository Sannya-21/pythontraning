class Employee:
    def __init__(self, emp_id, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_allowance(self):
        return self.salary * 0.20

    def calculate_deduction(self):
        return self.salary * 0.10

    def final_salary(self):
        return self.salary + self.calculate_allowance() - self.calculate_deduction()


# Employee IDs stored in list (array)
employee_ids = [101, 102, 103]

# Employee details stored in dictionary
employee_details = {
    101: {"name": "Ali", "salary": 30000},
    102: {"name": "Sara", "salary": 40000},
    103: {"name": "Ahmed", "salary": 50000}
}

print("----- Employee Salary Report -----")

for emp_id in employee_ids:
    try:
        emp = Employee(
            emp_id,
            employee_details[emp_id]["name"],
            employee_details[emp_id]["salary"]
        )

        print(f"\nEmployee ID : {emp.emp_id}")
        print(f"Name        : {emp.name}")
        print(f"Basic Salary: {emp.salary}")
        print(f"Allowance   : {emp.calculate_allowance()}")
        print(f"Deduction   : {emp.calculate_deduction()}")
        print(f"Final Salary: {emp.final_salary()}")

    except ValueError as e:
        print("Error:", e)