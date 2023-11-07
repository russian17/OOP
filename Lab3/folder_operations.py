from datetime import datetime
from operations import Operations
import os

class FolderOperations():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.commit_files = {}
        self.current_files = {}
        self.detected_files = []
        self.added_files_during_commit = {}
        self.deleted_files_during_commit = {}
        self.start_detection = False

    def get_file_info(self):
        files = {}
        for file in os.listdir(self.folder_path):
            if os.path.isfile(os.path.join(self.folder_path, file)):
                name, extension = file.rsplit('.', 1)
                created_time = os.path.getctime(os.path.join(self.folder_path, file))
                status = "Unmodified"
                modification_time = os.path.getmtime(os.path.join(self.folder_path, file))
                files[file] = [name, extension, status, created_time, modification_time]
        return files

    def commit(self):
        self.snapshot_time = datetime.now()
        print("Snapshot time updated to:", self.snapshot_time)
        self.commit_files = self.get_file_info()
        self.start_detection = True
        self.added_files_during_commit = {}
        self.deleted_files_during_commit = {}

    def status(self):
        if not self.commit_files:
            print("No snapshot has been created yet.")
            return

        self.current_files = self.get_file_info()
        print("Current files:")

        for file in self.current_files:
            if file not in self.commit_files:
                print(f"{file} - New file")
            elif self.current_files[file][4] > self.commit_files[file][4]:
                print(f"{file} - Modified")
            elif self.current_files[file][4] == self.commit_files[file][4]:
                print(f"{file} - Unmodified")

        deleted_files = set(self.commit_files.keys()) - set(self.current_files.keys())
        for file in deleted_files:
            print(f"{file} - Deleted")

        for file in self.deleted_files_during_commit:
            print(f"{file} - Deleted")

    def info(self):
        self.current_files = self.get_file_info()

        while True:
            operation = Operations(self.folder_path)
            print("What do you want to display?")
            print("1. All - all files")
            print("2. Image - image files")
            print("3. Text - text files")
            print("4. Program - program files")
            print("5. Go back - go back to main menu")
            print("6. Close - close the program")
            choice_info = input("Enter your choice:")

            if choice_info == "1":
                files = self.get_file_info()
                for file in files:
                    print(f"Filename - {files[file][0]}")
                    print(f"File extension: {files[file][1]}")
                    print(f"Created time: {files[file][3]}")
                    print(f"Modification time: {files[file][4]}")
                    print("--------------------------------------------------")

            elif choice_info == "2":
                operation.get_image_size()

            elif choice_info == "3":
                operation.count_texts()

            elif choice_info == "4":
                operation.program_processing()

            elif choice_info == "5":
                break

            elif choice_info == "6":
                print("Exiting the program.")
                exit()

            else:
                print("Invalid choice, try again!")
    def detection(self):
        if self.start_detection:
            self.current_files = self.get_file_info()
            added_files_during_commit = {}
            detected_files = []

            file_dict = {
                key: (
                    self.current_files.get(key) or
                    self.added_files_during_commit.get(key) or
                    self.commit_files.get(key)
                ) for key in
                set(self.current_files) | set(self.added_files_during_commit) | set(self.commit_files)
            }

            for file in self.current_files:
                if file not in self.commit_files and file not in self.detected_files:
                    print("DETECTION OCCURRED!:")
                    print(f"{file} - New file")
                    added_files_during_commit.update({file: self.current_files[file]})
                    detected_files.append(file)

                elif file in self.commit_files and file_dict[file][4] > self.commit_files[file][4]:
                    self.commit_files[file][4] = file_dict[file][4]
                    print("DETECTION OCCURRED!:")
                    print(f"{file} - Modified")
                    detected_files.append(file)

            deleted_files = set(file_dict.keys()) - set(self.current_files.keys())

            if deleted_files:
                for file in deleted_files:
                    if file in self.commit_files and file not in self.deleted_files_during_commit:
                        self.deleted_files_during_commit.update({file: self.commit_files[file]})
                        del self.commit_files[file]
                        print("DETECTION OCCURRED!:")
                        print(f"{file} - Deleted")

            self.detected_files += detected_files
            self.added_files_during_commit.update(added_files_during_commit)
#fff