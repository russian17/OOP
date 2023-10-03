def congratulations_enrolled(first_name, last_name, faculty_name, enrollment_date, template_file):
    with open(template_file, 'r') as file:
        message = file.read()

    message = message.replace("[Student's Name]", f"{first_name} {last_name}")
    message = message.replace("[Faculty Name]", faculty_name)
    message = message.replace("[Date]", enrollment_date)

    print(message)

# Example usage:
congratulations_enrolled("Sasha", "Gabi", "Fac1", "2023/2/2", "congrutalation_enrolling.txt")
