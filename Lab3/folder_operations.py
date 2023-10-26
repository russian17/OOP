class FolderOperations(Operations):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    # Function to list files from the folder with their status and modification time
    def list_files(self):
        files = {}
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                modification_time = os.path.getmtime(file_path)
                file_status = "NEW FILE"
                files[filename] = File(filename, file_status, modification_time)
        return files


    # Function to commit the snapshot and update the state of files by comparing memory size or name
    def commit(self):
        commit_count = 0

        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("Snapshot time updated to:", current_time)
        self.current_files = self.files

        if commit_count == 0:
            self.files = self.list_files()
            self.current_files = self.files
            commit_count += 1
            print("Commit done!")
            for filename, file_obj in self.files.items():
                print(f"File: {filename}, Status: {file_obj.status}, Modification Time: {file_obj.modification_time}")

            for filename, file_obj in self.current_files.items():
                print(f"File: {filename}, Status: {file_obj.status}, Modification Time: {file_obj.modification_time}")

            return

        self.files = self.list_files()
        for filename, file_obj in self.files.items():
            if filename in self.current_files:
                if file_obj.modification_time != self.current_files[filename].modification_time:
                    file_obj.status = "CHANGED"
                else:
                    file_obj.status = "NO CHANGED"
            else:
                file_obj.status = "NEW FILE"
        for filename, file_obj in self.current_files.items():
            if filename not in self.files:
                file_obj.status = "DELETED"
            if file_obj.status == "DELETED":
                del self.current_files[filename]
            if file_obj.status == "CHANGED":
                file_obj.status = "NO CHANGED"

        self.current_files = self.files
        commit_count += 1
        print("Commit done!")
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
                print("5. Go back - go back to main menu")
                print("6. Close - close the program")
                choice_info = input("Enter your choice:").lower()

                filenameArray, extensionArray = [], []
                for items in self.current_files:
                    filename, extension = items.rsplit('.', 1)
                    filenameArray.append(filename)
                    extensionArray.append(extension)

                if choice_info == "1":
                    for i in range(len(filenameArray)):
                        print(filenameArray[i] + "." + extensionArray[i])

                elif choice_info == "2":
                    self.process_images(filenameArray, extensionArray)

                elif choice_info == "3":
                    self.process_texts(filenameArray, extensionArray)

                elif choice_info == "4":
                    self.process_programs(filenameArray, extensionArray)

                elif choice_info == "5":
                    break

                elif choice_info == "6":
                    print("Exiting the program.")
                    exit()

                else:
                    print("Invalid choice, try again!")

# TODO:Change on current_files
    # Function to display status of files if they were changed since last snapshot comparing memory
    """def status(self):
        if not self.current_files:
            print("First need to commit!")
        else:
            for filename, file_obj in self.current_files.items():
                if file_obj.modification_time != self.files[filename].modification_time:
                    if file_obj.status == "NEW FILE":
                        print(f"{filename} - {file_obj.status}")
                    elif file_obj.status == "CHANGED":
                        print(f"{filename} - {file_obj.status}")
                    elif file_obj.status == "DELETED":
                        print(f"{filename} - {file_obj.status}")
                else:
                    if file_obj.status == "NO CHANGED":
                        print(f"{filename} - {file_obj}")
                    if filename not in self.files:
                        file_obj.status = "DELETED"""
