import os
import datetime as time


class File:
    def __init__(self, name, status):
        self.name = name
        self.status = status


class FolderOperations:
    def __init__(self, folder_path, snapshot_time):
        self.folder_path = folder_path
        self.snapshot_time = snapshot_time

    # Function to list files in the folder
    def list_files(self):
        files = []
        for item in os.listdir(self.folder_path):
            if os.path.isfile(os.path.join(self.folder_path, item)):
                files.append(item)
        return files

    # Function to print the contents of the folder with file extensions
    def print_folder_contents(self):
        for item in os.listdir(self.folder_path):
            if '.' in item:
                filename, extension = item.rsplit('.', 1)
                print(f"File: {filename}, Extension: {extension}")
            else:
                print(f"File: {item}, Extension: N/A")

    # Function to commit the snapshot and reset the state
    def commit(self):
        self.snapshot_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("Snapshot time updated to:", self.snapshot_time)
        self.list_files()


