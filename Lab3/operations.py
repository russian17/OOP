from PIL import Image
import re
import os

class Operations:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.text_content = None
        self.program_content = None


    def get_image_size(self):
        for file in os.listdir(self.folder_path):
            if file.endswith(("png", "jpg")):
                try:
                    with Image.open(os.path.join(self.folder_path, file)) as img:
                        width, height = img.size
                        print(f"{file} - {width}x{height}")
                except Exception as e:
                    print(f"Error: {str(e)}")

    def count_texts(self):
        for file in os.listdir(self.folder_path):
            line_count = 0
            word_count = 0
            char_count = 0
            if file.endswith("txt"):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r', encoding='utf-8') as file1:
                    text_content = file1.read()
                    self.text_content = text_content

                lines = text_content.split('\n')
                line_count += len(lines)

                words = text_content.split()
                word_count += len(words)

                char_count += len(text_content)

                print(f"{file} - {line_count} lines, {word_count} words, {char_count} characters")


    def program_processing(self):

        valid_extensions = ("py", "java", "cpp", "c")

        for file in os.listdir(self.folder_path):
            line_count = 0
            class_count = 0
            method_count = 0
            word_count = 0
            char_count = 0
            if file.endswith(valid_extensions):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r', encoding='utf-8') as file1:
                    program_content = file1.read()
                    self.program_content = program_content

                lines = program_content.split('\n')
                line_count += len(lines)

                class_pattern = r'\bclass\b'
                class_count += len(re.findall(class_pattern, program_content))

                method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
                method_count += len(re.findall(method_pattern, program_content))

                words = program_content.split()
                word_count += len(words)

                char_count += len(program_content)

                print(f"{file} - {line_count} lines, {class_count} classes, {method_count} methods, {word_count} words, {char_count} characters")