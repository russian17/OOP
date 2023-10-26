from folder_operations import FolderOperations
import threading
import time

class FolderManager():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.folder_operations = FolderOperations(folder_path)

    def schedule_detection(self):
        while True:
            self.folder_operations.detection(self.folder_path)
            time.sleep(5)  # Schedule detection every 5 seconds

    def run(self):
        # Create a thread for scheduled detection
        detection_thread = threading.Thread(target=self.schedule_detection)
        detection_thread.daemon = True  # Set the thread as a daemon, so it doesn't block program exit

        # Start the detection thread
        detection_thread.start()

        print("Welcome to Folder manager system!\n")
        while True:
            action = input("Enter action (commit, info <filename>, status, or exit): ")
            if action == "commit":
                self.folder_operations.commit()
            elif action.startswith("info"):
                _, filename = action.split(maxsplit=1)
                self.folder_operations.show_file_info(filename)
            elif action == "status":
                self.folder_operations.scan_folder()
                self.folder_operations.status()
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    folder_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test"
    file_manager = FolderManager(folder_path)
    file_manager.run()
