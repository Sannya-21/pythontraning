
# Patient class 
class Patient:
    def __init__(self, patient_id, name, age):
        if age <= 0:
            raise ValueError("Age must be greater than 0")

        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"

# Doctor Class

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"


# Data Structures
patient_records = {}      # Dictionary
patient_ids = []          # List
appointments = []         # List


# Add Patient Function

def add_patient():
    try:
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))

        patient = Patient(patient_id, name, age)

        patient_records[patient_id] = patient
        patient_ids.append(patient_id)

        print("Patient added successfully!")

    except ValueError as e:
        print("Invalid Patient Information:", e)


# -----------------------------
# Add Doctor Function
# -----------------------------
def add_doctor():
    doctor_id = int(input("Enter Doctor ID: "))
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")

    doctor = Doctor(doctor_id, name, specialization)

    print("Doctor Added:")
    print(doctor.display())


# -----------------------------
# Schedule Appointment
# -----------------------------
def schedule_appointment():
    try:
        patient_id = int(input("Enter Patient ID: "))

        if patient_id not in patient_records:
            raise KeyError("Patient ID not found")

        doctor_name = input("Enter Doctor Name: ")
        date = input("Enter Appointment Date: ")

        appointment = {
            "Patient ID": patient_id,
            "Doctor": doctor_name,
            "Date": date
        }

        appointments.append(appointment)

        print("Appointment Scheduled Successfully!")

    except KeyError as e:
        print("Error:", e)


# -----------------------------
# Display Patients
# -----------------------------
def display_patients():
    if not patient_records:
        print("No Patient Records Found")
        return

    for patient in patient_records.values():
        print(patient.display())



# Save Records to Fils
def save_records():
    with open("patient_records.txt", "w") as file:
        for patient in patient_records.values():
            file.write(patient.display() + "\n")

    print("Records saved to file successfully!")


# Main 
while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. Display Patients")
    print("5. Save Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        add_doctor()

    elif choice == "3":
        schedule_appointment()

    elif choice == "4":
        display_patients()

    elif choice == "5":
        save_records()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")