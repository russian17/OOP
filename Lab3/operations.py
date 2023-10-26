import struct
class Operations:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = {}
        self.current_files = {}
    def get_image_resolution(self, file_path):
        try:
            with open(file_path, 'rb') as img_file:
                data = img_file.read(24)
                if data.startswith(b'\x89PNG\r\n\x1a\n'):
                    width, height = struct.unpack('>ii', data[16:24])
                    return f"{width}x{height}"
                elif data[0:2] == b'\xFF\xD8':
                    jpeg_header = data[2:4]
                    while jpeg_header[0] == b'\xFF':
                        marker = jpeg_header[1]
                        data_length = struct.unpack(">H", img_file.read(2))[0]
                        img_file.seek(data_length - 2, 1)
                        jpeg_header = img_file.read(2)
                        if marker == 0xC0:
                            data = img_file.read(7)
                            height, width = struct.unpack(">HH", data[5:])
                            return f"{width}x{height}"

                return None
        except Exception as e:
            print(f"Error reading image: {str(e)}")
            return None

    def process_images(self, filenameArray, extensionArray):
        image_extensions = {"png", "jpg", "jpeg", "gif", "bmp"}
        found_images = False
        for i in range(len(filenameArray)):
            if extensionArray[i] in image_extensions:
                image_path = filenameArray[i] + "." + extensionArray[i]
                image_size = self.get_image_resolution(folder_path + "/" + image_path)
                if image_size:
                    print(f"{image_path} - {image_size}")
                found_images = True
        if not found_images:
            print("No images found!")

    # Function to line, word and character count from a file
    def count_texts(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = words = characters = 0
                for line in file:
                    lines += 1
                    words += len(line.split())
                    characters += len(line)
                return lines, words, characters
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return None

    def process_texts(self, filenameArray, extensionArray):
        text_extensions = {"txt", "pdf", "docx", "rtf"}
        found_texts = False
        for i in range(len(filenameArray)):
            if extensionArray[i] in text_extensions:
                print(filenameArray[i] + "." + extensionArray[i])
                text_path = filenameArray[i] + "." + extensionArray[i]
                text_count = self.count_texts(folder_path + "/" + text_path)
                if text_count:
                    print(f"Lines: {text_count[0]}, Words: {text_count[1]}, Characters: {text_count[2]}")
                found_texts = True
        if not found_texts:
            print("No texts found!")

    # Function to count lines, classes and functions from a program file
    def count_programs(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = classes = functions = 0
                for line in file:
                    lines += 1
                    if line.startswith("class"):
                        classes += 1
                    elif line.startswith("def"):
                        functions += 1
                return lines, classes, functions
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return None

    def process_programs(self, filenameArray, extensionArray):
        program_extensions = {"py", "java", "cpp", "c"}
        found_programs = False
        for i in range(len(filenameArray)):
            if extensionArray[i] in program_extensions:
                print(filenameArray[i] + "." + extensionArray[i])
                program_path = filenameArray[i] + "." + extensionArray[i]
                program_count = self.count_programs(folder_path + "/" + program_path)
                if program_count:
                    print(f"Lines: {program_count[0]}, Classes: {program_count[1]}, Functions: {program_count[2]}")
                found_programs = True
        if not found_programs:
            print("No programs found!")