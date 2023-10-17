from claaas import FolderOperations  # Assuming 'FolderOperations' is in the 'class' module

class FolderManager:
    def __init__(self):
        self.folder_path = "C:\\Users\\Simion\\Desktop\\OOP\\Lab3\\Test"
        self.FolderOperations = FolderOperations(self.folder_path, None)  # Pass None as the initial snapshot_time

    def run(self):
        print("Welcome to Folder manager system!\n")
        menu_options = {
            1: self.FolderOperations.commit,
            2: self.FolderOperations.print_folder_contents,  # You can use print_folder_contents to list files
            3: self.FolderOperations.get_status,  # Use get_status to display file status
            4: self.print,  # Modify this to call your custom function
            5: lambda: (print("Exiting the program.") or exit())
        }

        while True:
            print("What do you want to do ?")
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

if __name__ == "__main__":
    file = FolderManager()
    file.run()
