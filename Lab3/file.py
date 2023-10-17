import time
import os

class File:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class FolderOperations:
    def __init__(self, folder_path, snapshot_time):
        self.folder_path = folder_path
        self.snapshot_time = snapshot_time
        self.files = {}

    # Function to list files in the folder
    def list_files(self):
        return os.listdir(self.folder_path)

    # Function to commit the snapshot and update the state
    # Function to commit the snapshot and update the state
    # Function to commit the snapshot and update the state
    def commit(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("Snapshot time updated to:", current_time)

        current_files = self.list_files()

        for filename, file_obj in self.files.items():
            if filename in current_files:
                if file_obj.status != "NEW FILE":
                    file_obj.status = "NO CHANGED"
                else:
                    file_obj.status = "CHANGED"
            else:
                file_obj.status = "DELETED"

        for filename in current_files:
            if filename not in self.files:
                self.files[filename] = File(filename, "NEW FILE")

        # Update snapshot time after processing all changes
        self.snapshot_time = current_time

        # Trace changes
        for filename, file_obj in self.files.items():
            print(f"File: {filename}, Status: {file_obj.status}")


class FolderManager:
    def __init__(self):
        self.folder_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test"
        self.FolderOperations = FolderOperations(self.folder_path, None)

    def run(self):
        print("Welcome to Folder manager system!\n")
        menu_options = {
            1: self.FolderOperations.commit,
            2: self.FolderOperations.commit,  # Change this to print_folder_contents
            3: self.FolderOperations.commit,  # Change this to get_status
            4: self.custom_function,  # Add your custom function here
            5: lambda: (print("Exiting the program.") or exit())
        }

        while True:
            print("What do you want to do?")
            print("1 - Commit snapshot and update status\n")
            print("2 - Print folder contents\n")
            print("3 - Get file status\n")
            print("4 - Your custom function\n")
            print("5 - Quit the program\n")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric choice.")
                continue

            if choice in menu_options:
                if choice == 5:
                    menu_options[choice]()  # Execute lambda function
                    break
                else:
                    menu_options[choice]()  # Execute the corresponding method
            else:
                print("Invalid choice. Please select a valid option.")

    def custom_function(self):
        # Implement your custom function here
        print("Custom function called.")

if __name__ == "__main__":
    file = FolderManager()
    file.run()
