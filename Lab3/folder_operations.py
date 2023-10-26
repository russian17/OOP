from datetime import datetime
import os
from operations import Operations
class FolderOperations():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.file_info = {}
        self.previous_file_list = set()
        self.previous_file_info = {}
        self.processed_files = set()

    def commit(self):
        self.snapshot_time = datetime.now()
        self.previous_file_list = set(self.file_info.keys())
        self.previous_file_info = self.file_info.copy()
        self.file_info = {}
        print(f"Snapshot updated at {self.snapshot_time}")

    def scan_folder(self):
        print(f"Scanning folder: {self.folder_path}")
        files = os.listdir(self.folder_path)
        print(f"Files in folder: {files}")
        for file in files:
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                self.update_file_info(file_path)

    def update_file_info(self, file_path):
        file_info = {}
        file_info["name"] = os.path.relpath(file_path, self.folder_path)
        file_info["extension"] = os.path.splitext(file_path)[1]
        file_info["created_time"] = datetime.fromtimestamp(os.path.getctime(file_path))
        file_info["modified_time"] = datetime.fromtimestamp(os.path.getmtime(file_path))

        if file_info["extension"] in {".png", ".jpg", ".jpeg", ".gif", ".bmp"}:
            Operation = Operations(file_path)
            file_info["image_size"] = Operation.get_image_size()
        elif file_info["extension"] in {".txt", ".pdf", ".docx", ".rtf"}:
            Operation = Operations(file_path)
            line_count, word_count, char_count = Operation.get_text_stats()
            file_info["line_count"] = line_count
            file_info["word_count"] = word_count
            file_info["char_count"] = char_count
        elif file_info["extension"] in {".py", "java", "cpp", "c"}:
            Operation = Operations(file_path)
            line_count, class_count, method_count, word_count, char_count = Operation.program_processing()
            file_info["line_count"] = line_count
            file_info["class_count"] = class_count
            file_info["method_count"] = method_count
            file_info["word_count"] = word_count
            file_info["char_count"] = char_count

        self.file_info[file_info["name"]] = file_info

    def show_file_info(self, filename):
        if filename in self.file_info:
            print(self.file_info)
            file_info = self.file_info[filename]
            print("File Name:", file_info["name"])
            print("Extension:", file_info["extension"])
            print("Created Time:", file_info["created_time"])
            print("Modified Time:", file_info["modified_time"])
            if "image_size" in file_info:
                print("Image Size:", file_info["image_size"])
            elif "line_count" in file_info:
                print("Line Count:", file_info["line_count"])
                if "word_count" in file_info:
                    print("Word Count:", file_info["word_count"])
                else:
                    print("Word Count: N/A")
                if "char_count" in file_info:
                    print("Character Count:", file_info["char_count"])
                else:
                    print("Character Count: N/A")
            if "class_count" in file_info:
                print("Class Count:", file_info["class_count"])
            if "method_count" in file_info:
                print("Method Count:", file_info["method_count"])
        else:
            print(f"File '{filename}' not found in the monitored folder.")

    def status(self):
        if self.snapshot_time:
            print(f"Snapshot taken at {self.snapshot_time}")

            # Use the set of previous file names to identify added and deleted files
            added_files = self.file_info.keys() - self.previous_file_list
            deleted_files = self.previous_file_list - self.file_info.keys()

            # Handle added files
            for filename in added_files:
                file_info = self.file_info[filename]
                # Check if the file was created after the snapshot time
                if file_info["created_time"] > self.snapshot_time:
                    print(f"{filename} - New File")

            # Handle deleted files
            for filename in deleted_files:
                print(f"{filename} - Deleted")

            # Iterate over the current file info to check for changes
            for filename, file_info in self.file_info.items():
                prev_info = self.previous_file_info.get(filename)
                if prev_info:
                    if file_info != prev_info:
                        print(f"{filename} - Changed")
                    else:
                        print(f"{filename} - No change")

    def detection(self, file_path):
        if self.snapshot_time:
            file_info = {}
            file_info["name"] = os.path.relpath(file_path, self.folder_path)
            file_info["extension"] = os.path.splitext(file_path)[1]
            file_info["created_time"] = datetime.fromtimestamp(os.path.getctime(file_path))
            file_info["modified_time"] = datetime.fromtimestamp(os.path.getmtime(file_path))
            for filename, file_info in self.file_info.items():
                if file_info["name"] in self.file_info and file_info["name"] in self.previous_file_info:
                    if file_info["modified_time"] > self.snapshot_time:
                        print(f"{file_info['name']} - Changed")
            for filename, file_info in self.file_info.items():
                self.processed_files.add(filename)
                if filename not in self.processed_files:
                    if file_info["created_time"] > self.snapshot_time:
                        print(f"{file_info['name']} - New File")

                #elif file_info["name"] in self.file_info and file_info["name"] not in self.previous_file_info:
                    #print(f"{file_info['name']} - File deleted")




