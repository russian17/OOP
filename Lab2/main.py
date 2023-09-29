import Student_class
from General_operations import input_faculty,  display_faculties, display_faculties_by_field, search_student_what_faculty
from Faculty_operations import display_enrolled_students, display_graduated_students, student_belongs_to_faculty, assign_student_to_faculty, graduate_student
from Student_operations import delete_student_by_email
class UTM:
    def __init__(self):
        self.file_name_enrolled = "current_enrolled_students.json"
        self.file_name_faculties = "faculties.json"
        self.file_name_graduates = "graduatedstudents.json"


    def run(self):
        while True:
            print("Welcome to TUM's student manager system!\n")
            print("What do you want to do?\n")
            print("g - General operations\n")
            print("f - Faculty operations\n")
            print("s - Student operations\n")
            print("\n")
            print("q - Quit the program")
            choice = input("Enter your choice: ")

            if choice == "g":
                while True:
                    print("General operations\n")
                    print("What do you want to do ?")
                    print("1 - Create a faculty\n")
                    print("2 - Search what faculty students belongs to\n")
                    print("3 - Display university faculties\n")
                    print("4 - Display all faculties belonging to a field\n")
                    print("5 - Back\n")
                    print("6 - Quit the program\n\n")
                    while True:
                        try:
                            choice_g = int(input("Enter your choice: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric choice.")
                    if choice_g == 1:
                        input_faculty()
                    elif choice_g == 2:
                        search_student_what_faculty()
                    elif choice_g == 3:
                        display_faculties(self.file_name_faculties)
                    elif choice_g == 4:
                        display_faculties_by_field(self.file_name_faculties)
                    elif choice_g == 5:
                        break
                    elif choice_g == 6:
                        print("Exiting the program.")
                        return
                    else:
                        print("Invalid choice. Please select a valid option.")
            elif choice == "f":
                while True:
                    print("Faculty operations\n")
                    print("What do you want to do ?")
                    print("1 - Assign student to a faculty\n")
                    print("2 - Create a student and directly assign to a faculty\n")
                    print("3 - Graduate a student from a faculty\n")
                    print("4 - Display current enrolled students\n")
                    print("5 - Display graduates\n")
                    print("6 - Tell or not if student belongs to this faculty\n")
                    print("7 - Back\n")
                    print("8 - Quit the program\n")
                    while True:
                        try:
                            choice_f = int(input("Enter your choice: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric choice.")
                    if choice_f == 1:
                        assign_student_to_faculty()
                    elif choice_f == 2:
                        Student_class.Student.input_and_assign_student(self)
                    elif choice_f == 3:
                        graduate_student()
                    elif choice_f == 4:
                        display_enrolled_students(self.file_name_enrolled)
                    elif choice_f == 5:
                        display_graduated_students(self.file_name_graduates)
                    elif choice_f == 6:
                        student_belongs_to_faculty(self.file_name_faculties)
                    elif choice_f == 7:
                        break
                    elif choice_f == 8:
                        print("Exiting the program.")
                        return
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "s":
                while True:
                    print("Student operations\n")
                    print("What do you want to do ?")
                    print("1 - Enroll student to university\n")
                    print("2 - Kick student from university\n")
                    print("3 - Back\n")
                    print("4 - Quit the program\n")
                    while True:
                        try:
                            choice_s = int(input("Enter your choice: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric choice.")
                    if choice_s == 1:
                        Student_class.Student.input_student(self)
                    elif choice_s == 2:
                        email = input("Input email of which student you want to kick:")
                        delete_student_by_email(email)
                    elif choice_s == 3:
                        break
                    elif choice_s == 4:
                        print("Exiting the program.")
                        return
                    else:
                        print("Invalid choice. Please select a valid option.")


            elif choice == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    utm = UTM()
    utm.run()
