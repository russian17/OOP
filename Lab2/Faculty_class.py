import json
import os


class Faculty:
    def __init__(self, Name, Abbreviation, Study_Field):
        self.Name = Name
        self.Abbreviation = Abbreviation
        self.Student1 = []
        self.Study_Field = Study_Field



    def add_to_file_faculties(self, file_name):
        faculties = []

        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            # Check if the file exists and is not empty
            with open(file_name, 'r') as file:
                try:
                    faculties = json.load(file)
                except json.JSONDecodeError:
                    print("Error: The file contains invalid JSON data. Creating a new file.")

        faculties.append(self.to_dict())

        with open(file_name, 'w') as file:
            json.dump(faculties, file, indent=4)

    def to_dict(self):
        # Convert the student object to a dictionary
        faculties_dict = {
            'Name': self.Name,
            'Abbreviation': self.Abbreviation,
            'Student1': self.Student1,
            'Study_Field': self.Study_Field

        }
        return faculties_dict
