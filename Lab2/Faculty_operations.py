import json
import os


def assign_student_to_faculty():
    while True:
        # Checks faculty existence
        faculty_abbr = input("Enter the faculty abbreviation: ")
        with open("faculties.json", 'r') as faculty_file:
            faculties_data = json.load(faculty_file)

        while True:
            faculty_found = False

            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    faculty_found = True
                    break

            if faculty_found:
                break
            else:
                print("Faculty does not exist, try again!")
                faculty_abbr = input("Enter the faculty abbreviation: ")
        student_email = input("Enter the student's email: ")

        # Load faculty data from faculties.json
        with open("faculties.json", 'r') as faculty_file:
            faculties_data = json.load(faculty_file)

        # Search for the faculty by abbreviation
        faculty_found = False
        for faculty in faculties_data:
            if faculty["Abbreviation"] == faculty_abbr:
                faculty["Student1"].append(student_email)
                faculty_found = True
                break

        if not faculty_found:
            print(f"Faculty with abbreviation '{faculty_abbr}' not found.")

        # Load student data from current_enrolled_students.json
        with open("current_enrolled_students.json", 'r') as student_file:
            students_data = json.load(student_file)

        # Check if the student exists
        student_found = False
        for student in students_data:
            if student["email"] == student_email:
                student_found = True
                break

        if not student_found:
            print(f"Student with email '{student_email}' not found.")

        # Save the updated faculty data back to faculties.json
        with open("faculties.json", 'w') as faculty_file:
            json.dump(faculties_data, faculty_file, indent=4)

        another = input("Do you want to input another student? (yes/no): ").lower()
        if another != "yes":
            print("Exiting the program.")
            break
        print(f"Student with email '{student_email}' added successfully to faculty '{faculty_abbr}'. ")

def graduate_student():
    while True:
        graduated_email = input("Enter the student's email: ")
        with open("current_enrolled_students.json", 'r') as enrolled_file:
            enrolled_data = json.load(enrolled_file)

        while True:
            # Checks student existence
            student_found = False

            for student in enrolled_data:
                if student["email"] == graduated_email:
                    student_found = True
                    break

            if student_found:
                break
            else:
                print("Student with this email does not exist, try again!")
                graduated_email = input("Enter the student's email: ")

        # Load current enrolled students
        current_enrolled_file = "current_enrolled_students.json"
        enrolled_students = []

        if os.path.exists(current_enrolled_file) and os.path.getsize(current_enrolled_file) > 0:
            with open(current_enrolled_file, 'r') as enrolled_file:
                enrolled_students = json.load(enrolled_file)

        # Remove the graduated student from the list of enrolled students
        updated_enrolled_students = [student for student in enrolled_students if student['email'] != graduated_email]

        # Save the updated list back to current_enrolled_students.json
        with open(current_enrolled_file, 'w') as enrolled_file:
            json.dump(updated_enrolled_students, enrolled_file, indent=4)

        # Load faculties data
        faculties_file = "faculties.json"
        faculties_data = []

        if os.path.exists(faculties_file) and os.path.getsize(faculties_file) > 0:
            with open(faculties_file, 'r') as faculty_file:
                faculties_data = json.load(faculty_file)

        # Iterate through faculties and remove the graduated student from their lists
        for faculty in faculties_data:
            if graduated_email in faculty["Student1"]:
                faculty["Student1"].remove(graduated_email)

        # Save the updated faculties data back to faculties.json
        with open(faculties_file, 'w') as faculty_file:
            json.dump(faculties_data, faculty_file, indent=4)

        # Move the graduated student to the graduatedstudents.json file
        graduated_students_file = "graduatedstudents.json"
        graduated_students = []

        if os.path.exists(graduated_students_file) and os.path.getsize(graduated_students_file) > 0:
            with open(graduated_students_file, 'r') as graduated_file:
                graduated_students = json.load(graduated_file)

        # Find the student data in enrolled students
        graduated_student_data = next((student for student in enrolled_students if student['email'] == graduated_email), None)


        # Add the graduated student data to the graduated students list
        graduated_students.append(graduated_student_data)

        # Save the updated list to graduatedstudents.json
        with open(graduated_students_file, 'w') as graduated_file:
            json.dump(graduated_students, graduated_file, indent=4)

        print("Student graduated successfully!")
        print(f"Congratulations {graduated_email} for graduating UTM")
        another = input("Do you want to graduate another student? (yes/no): ").lower()
        if another != "yes":
            break



def display_enrolled_students(file_name_enrolled):
    try:
        with open(file_name_enrolled, 'r') as enrolled_file:
            students_data = json.load(enrolled_file)
            for student in students_data:
                print("First Name:", student["first_name"])
                print("Last Name:", student["last_name"])
                print("Email:", student["email"])
                print("Enrollment Date:", student["enrollment_date"])
                print("Date of Birth:", student["date_of_birth"])
                print()
    except FileNotFoundError:
        print(f"The '{file_name_enrolled}' file does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The '{file_name_enrolled}' file contains invalid JSON data.")

def display_graduated_students(file_name_graduates):
    try:
        with open(file_name_graduates, 'r') as graduates_file:
            students_data = json.load(graduates_file)
            for student in students_data:
                print("First Name:", student["first_name"])
                print("Last Name:", student["last_name"])
                print("Email:", student["email"])
                print("Enrollment Date:", student["enrollment_date"])
                print("Date of Birth:", student["date_of_birth"])
                print()
    except FileNotFoundError:
        print(f"The '{file_name_graduates}' file does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The '{file_name_graduates}' file contains invalid JSON data.")

def student_belongs_to_faculty(file_name_faculties):
    while True:
        # Checks faculty
        faculty_abbr = input("Enter the faculty abbreviation: ")
        with open("faculties.json", 'r') as faculty_file:
            faculties_data = json.load(faculty_file)

        while True:
            faculty_found = False

            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    faculty_found = True
                    break

            if faculty_found:
                break
            else:
                print("Faculty does not exist, try again!")
                faculty_abbr = input("Enter the faculty abbreviation: ")

        student_email = input("Enter the student's email: ")
        with open("current_enrolled_students.json", 'r') as enrolled_file:
            enrolled_data = json.load(enrolled_file)

        while True:
            # Checks student existence
            student_found = False

            for student in enrolled_data:
                if student["email"] == student_email:
                    student_found = True
                    break

            if student_found:
                break
            else:
                print("Student with this email does not exist, try again!")
                student_email = input("Enter the student's email: ")


        with open(file_name_faculties, 'r') as faculty_file:
            faculties_data = json.load(faculty_file)

            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    if student_email in faculty["Student1"]:
                        print(
                            f"The student with email '{student_email}' belongs to the faculty '{faculty['Name']}'.")
                    else:
                        print(
                            f"The student with email '{student_email}' does not belong to the faculty '{faculty['Name']}'.")

        another = input("Do you want to find another student? (yes/no): ").lower()
        if another != "yes":
            break
