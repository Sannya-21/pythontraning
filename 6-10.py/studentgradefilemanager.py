import csv

def calculate_grade(marks):
    """Return grade based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def process_students(input_file, output_file):
    try:
        with open(input_file, "r", newline="") as infile, \
             open(output_file, "w", newline="") as outfile:

            reader = csv.DictReader(infile)

            fieldnames = ["Name", "Marks", "Grade"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                marks = int(row["Marks"])
                grade = calculate_grade(marks)

                writer.writerow({
                    "Name": row["Name"],
                    "Marks": marks,
                    "Grade": grade
                })

        print(f"Results successfully saved to '{output_file}'")

    except FileNotFoundError:
        print("Error: Input file not found.")

    except ValueError:
        print("Error: Invalid marks value in CSV file.")

    except Exception as e:
        print("An error occurred:", e)


# Main Program
input_csv = "students.csv"
output_csv = "results.csv"

process_students(input_csv, output_csv)