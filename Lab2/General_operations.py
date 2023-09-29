import json
from Faculty_class import Faculty

def input_faculty():
    # The only valid Study Field
    study_fields = ["Mechanical_Engineering", "Software_Engineering", "Food_Technology", "Urbanism_Architecture",
                    "Veterinary_Medicine"]

    while True:
        Name = input("Enter faculty name: ")
        Abbreviation = input("Enter abbreviation: ")
        print("Available fields:Mechanical_Engineering, Software_Engineering,"
              " Food_Technology, Urbanism_Architecture, Veterinary_Medicine")
        Study_Field = input("Enter Study_Field: ")
        while Study_Field not in study_fields:
            # Checking valid study field
            print("Wrong field, try again")
            Study_Field = input("Enter Study_Field: ")

        student = Faculty(Name, Abbreviation, Study_Field)
        student.add_to_file_faculties("faculties.json")

        print("Faculty added successfully.")
        another = input("Do you want to add another faculty? (yes/no): ").lower()
        if another != "yes":
            break

def search_student_what_faculty():
    while True:
        gmail_check = input("Enter the student's email: ")
        with open("current_enrolled_students.json", 'r') as enrolled_file:
            enrolled_data = json.load(enrolled_file)

        while True:
            # Checks student
            student_found = False

            for student in enrolled_data:
                if student["email"] == gmail_check:
                    student_found = True
                    break

            if student_found:
                break
            else:
                print("Student with this email does not exist, try again!")
                gmail_check = input("Enter the student's email: ")

        try:
            with open("faculties.json", 'r') as faculty_file:
                faculties_data = json.load(faculty_file)

                for faculty in faculties_data:
                    students_list = [student.lower() for student in faculty.get("Student1", [])]
                    if gmail_check in students_list:
                        print("Faculty for student with email", gmail_check)
                        print("Name:", faculty["Name"])
                        print("Abbreviation:", faculty["Abbreviation"])
                        print("Student1:", ", ".join(faculty.get("Student1", [])))
                        print("Study Field:", faculty["Study_Field"])
                        return

                print("Student with email", gmail_check, "not found in any faculty.")
        except FileNotFoundError:
            print(f"The  file does not exist.")
        except json.JSONDecodeError:
            print(f"Error: The file contains invalid JSON data.")

        another = input("Do you want to search another student? (yes/no): ").lower()
        if another != "yes":
            break

def display_faculties(file_name_faculties):
    try:
        with open(file_name_faculties, 'r') as faculty_file:
            faculties_data = json.load(faculty_file)
            for faculty in faculties_data:
                print("Name:", faculty["Name"])
                print("Abbreviation:", faculty["Abbreviation"])
                print("Students:", faculty["Student1"])
                print("Study Field:", faculty["Study_Field"])
                print()
    except FileNotFoundError:
        print(f"The '{file_name_faculties}' file does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The '{file_name_faculties}' file contains invalid JSON data.")

def display_faculties_by_field(file_name_faculties):
    study_fields = ["Mechanical_Engineering", "Software_Engineering", "Food_Technology", "Urbanism_Architecture", "Veterinary_Medicine"]

    while True:
        print("Available fields:Mechanical_Engineering, Software_Engineering,"
              " Food_Technology, Urbanism_Architecture, Veterinary_Medicine")
        field = input("Enter the field whose faculties you want to display: ")
        if field not in study_fields:
            print("Wrong field, try again")
        else:
            try:
                with open(file_name_faculties, 'r') as faculty_file:
                    faculties_data = json.load(faculty_file)
                    for faculty in faculties_data:
                        if faculty["Study_Field"] == field:
                            print("Name:", faculty["Name"])
                            print("Abbreviation:", faculty["Abbreviation"])
                            print("Students:", faculty["Student1"])
                            print("Study Field:", faculty["Study_Field"])
                            print()
                break
            except FileNotFoundError:
                print(f"The '{file_name_faculties}' file does not exist.")
            except json.JSONDecodeError:
                print(f"Error: The '{file_name_faculties}' file contains invalid JSON data.")

