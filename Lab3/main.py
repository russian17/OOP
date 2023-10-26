
class FolderManager(FolderOperations):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    def run(self):
        print("Welcome to Folder manager system!\n")
        menu_options = {
            1: self.commit,
            2: self.info,
            3: self.status,
            4: lambda: (print("Exiting the program.") or exit())
        }

        while True:
            print("What do you want to do?")
            print("1 - Commit snapshot and update status\n")
            print("2 - Print folder contents\n")
            print("3 - Get file status\n")
            print("4 - Quit the program\n")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric choice.")
                continue

            if choice in menu_options:
                if choice == 4:
                    menu_options[choice]()
                    break
                else:
                    menu_options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    folder_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test"
    file = FolderManager(folder_path)
    file.run()

