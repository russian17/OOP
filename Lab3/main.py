import time
import os

class File:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class FolderOperations:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = {}
        self.current_files = {}

    # Function to list files in the folder
    def list_files(self):
        return os.listdir(self.folder_path)
# TODO Updates on current_files and files with it status
    # Function to commit the snapshot and update the state
    def commit(self):
        global current_time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("Snapshot time updated to:", current_time)

        self.current_files = self.list_files()

        for filename, file_obj in self.files.items():
            if filename in self.current_files:
                if file_obj.status != "NEW FILE":
                    file_obj.status = "NO CHANGED"
                else:
                    file_obj.status = "CHANGED"
            else:
                file_obj.status = "DELETED"

        for filename in self.current_files:
            if filename not in self.files:
                self.files[filename] = File(filename, "NEW FILE")

        # Update snapshot time after processing all changes
        self.snapshot_time = current_time

        # Trace changes
        for filename, file_obj in self.files.items():
            print(f"File: {filename}, Status: {file_obj.status}")

        print(self.files)
        print(self.current_files)

    # Function to display info by criteria
    def info(self):
        if not self.current_files:
            print("First need to commit!")
        else:
            while True:
                print("What do you want to display?")
                print("1. All - all files")
                print("2. Image - image files")
                print("3. Text - text files")
                print("4. Program - program files")
                print("5. Close - close the program")
                choice_info = input("Enter your choice:").lower()

                filenameArray, extensionArray = [], []
                for items in self.current_files:
                    filename, extension = items.rsplit('.', 1)
                    filenameArray.append(filename)
                    extensionArray.append(extension)

                if choice_info == "all":
                    for i in range(len(filenameArray)):
                        print(filenameArray[i] + "." + extensionArray[i])

                elif choice_info == "image":
                    image_extensions = {"png", "jpg", "jpeg", "gif", "bmp"}
                    found_images = False
                    for i in range(len(filenameArray)):
                        if extensionArray[i] in image_extensions:
                            print(filenameArray[i] + "." + extensionArray[i])
                            found_images = True
                    if not found_images:
                        print("No images found!")

                elif choice_info == "text":
                    text_extensions = {"txt", "pdf", "docx", "rtf"}
                    found_texts = False
                    for i in range(len(filenameArray)):
                        if extensionArray[i] in text_extensions:
                            print(filenameArray[i] + "." + extensionArray[i])
                            found_texts = True
                    if not found_texts:
                        print("No texts found!")

                elif choice_info == "program":
                    program_extensions = {"py", "java", "cpp", "c"}
                    found_programs = False
                    for i in range(len(filenameArray)):
                        if extensionArray[i] in program_extensions:
                            print(filenameArray[i] + "." + extensionArray[i])
                            found_programs = True
                    if not found_programs:
                        print("No programs found!")

                elif choice_info == "close":
                    print("Exiting the program.")
                    exit()

                else:
                    print("Invalid choice, try again!")

# TODO:Change on current_files
    # Function to display status
    def status(self):
        for filename, file_obj in self.files.items():
            print(f"{filename} - Status: {file_obj.status}")


class FolderManager(FolderOperations):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    def run(self):
        print("Welcome to Folder manager system!\n")
        menu_options = {
            1: self.commit,
            2: self.info,
            3: self.status,
            4: self.custom_function,
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
    folder_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test"
    file = FolderManager(folder_path)
    file.run()
