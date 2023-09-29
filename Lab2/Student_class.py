import json
import os
import datetime

class Student:
    def __init__(self, first_Name, last_Name, email, enrollment_Date, date_birth):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.email = email
        self.enrollment_Date = self.validate_date(enrollment_Date)
        self.date_birth = self.validate_date(date_birth)

    #Function for inputting correct date
    def validate_date(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y/%m/%d')
            return date_obj
        except ValueError:
            raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

    def input_student(self):
        while True:
            first_Name = input("Enter first name: ")
            last_Name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate enrollment date and date of birth
            while True:
                enrollment_Date = input("Enter enrollment date (yyyy/mm/dd): ")
                try:
                    Student.validate_date(self, enrollment_Date)
                    break
                except ValueError as e:
                    print(e)

            while True:
                # Checks date
                date_birth = input("Enter date of birth (yyyy/mm/dd): ")
                try:
                    Student.validate_date(self, date_birth)
                    break
                except ValueError as e:
                    print(e)

            try:
                student = Student(first_Name, last_Name, email, enrollment_Date, date_birth)
                student.add_to_file_enrolled("current_enrolled_students.json")
                print(f"Student {first_Name}, added successfully.")
            except ValueError as e:
                print(e)

            another = input("Do you want to add another student? (yes/no): ").lower()
            if another != "yes":
                break

    def input_and_assign_student(self):
        while True:
            first_Name = input("Enter first name: ")
            last_Name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate enrollment date and date of birth
            while True:
                enrollment_Date = input("Enter enrollment date (yyyy/mm/dd): ")
                try:
                    Student.validate_date(self, enrollment_Date)
                    break
                except ValueError as e:
                    print(e)

            while True:
                # Checks date
                date_birth = input("Enter date of birth (yyyy/mm/dd): ")
                try:
                    Student.validate_date(self, date_birth)
                    break
                except ValueError as e:
                    print(e)

            try:
                student = Student(first_Name, last_Name, email, enrollment_Date, date_birth)
                student.add_to_file_enrolled("current_enrolled_students.json")
            except ValueError as e:
                print(e)

            student_email = email
            faculty_abbr = input("Enter the faculty abbreviation: ")
            with open("faculties.json", 'r') as faculty_file:
                faculties_data = json.load(faculty_file)

            while True:
                # Checks faculty existence
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

            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    faculty["Student1"].append(student_email)
                    break

            with open("faculties.json", 'w') as faculty_file:
                json.dump(faculties_data, faculty_file, indent=4)

            print(f"Student {first_Name}, added and assigned successfully.")
            another = input("Do you want to add and assign another student? (yes/no): ").lower()
            if another != "yes":
                break

    def add_to_file_enrolled(self, file_name):
        students = []

        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            # Check if the file exists and is not empty
            with open(file_name, 'r') as file:
                try:
                    students = json.load(file)
                except json.JSONDecodeError:
                    print("Error: The file contains invalid JSON data. Creating a new file.")

        students.append(self.to_dict())

        with open(file_name, 'w') as file:
            json.dump(students, file, indent=4)

    def to_dict(self):
        # Convert the student object to a dictionary
        student_dict = {
            'first_name': self.first_Name,
            'last_name': self.last_Name,
            'email': self.email,
            'enrollment_date': self.enrollment_Date.strftime('%Y/%m/%d'),  # Format date as a string
            'date_of_birth': self.date_birth.strftime('%Y/%m/%d')  # Format date as a string
        }
        return student_dict


