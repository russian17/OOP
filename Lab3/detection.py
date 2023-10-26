from folder_operations import FolderOperations
import os
class Detection():
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def changes_detection(self):
        current_file_list = set(self.file_info.keys())
        added_files = current_file_list - self.previous_file_list
        deleted_files = self.previous_file_list - current_file_list

        for filename, file_info in self.file_info.items():
            if filename in added_files:
                print(f"{filename} - New File")
            elif filename in deleted_files:
                print(f"{filename} - Deleted")
            elif filename not in deleted_files and os.path.exists(os.path.join(self.folder_path, filename)):
                if file_info["modified_time"] > self.snapshot_time:
                    print(f"{filename} - Changed")
            else:
                print(f"{filename} - File deleted")