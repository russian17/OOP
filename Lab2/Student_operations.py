import json
import os
import Faculty_class as faculty
def delete_student_by_email(email):
    while True:
        # Load current enrolled students
        current_enrolled_file = "current_enrolled_students.json"
        current_faculties_file = "faculties.json"
        if os.path.exists(current_enrolled_file) and os.path.getsize(current_enrolled_file) > 0:
            with open(current_enrolled_file, 'r') as enrolled_file:
                enrolled_students = json.load(enrolled_file)
            with open(current_faculties_file, 'r') as faculties_file:
                faculties = json.load(faculties_file)
        else:
            enrolled_students = []

        # Check if the student exists in the list
        student_to_delete = None
        for student in enrolled_students:
            if student['email'] == email:
                student_to_delete = student
                break

        if student_to_delete:
            # Remove the student from the list
            enrolled_students.remove(student_to_delete)

            # Save the updated list back to current_enrolled_students.json
            with open(current_enrolled_file, 'w') as enrolled_file:
                json.dump(enrolled_students, enrolled_file, indent=4)
            with open(current_faculties_file, 'w') as faculties_file:
                json.dump(enrolled_students, faculties_file, indent=4)
            found_student = True
            for students in faculties:
                if email == faculty['Student1']:
                    faculty['Students1'].remove(email)
            print(f"Student with email '{email}' has been deleted.")
        else:
            print(f"Student with email '{email}' not found in the list.")

        print(f"Student with email {email} deleted successfully.")
        another = input("Do you want to delete another student? (yes/no): ").lower()
        if another != "yes":
            break
