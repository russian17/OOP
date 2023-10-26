from PIL import Image
import re
import os

class Operations:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.content = None

    def get_image_size(self):
        if self.folder_path.endswith((".png", ".jpg")):
            try:
                with Image.open(self.folder_path) as img:
                    width, height = img.size
                    return f"{width}x{height}"
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "Not an image file"

    def count_texts(self):
        try:
            with open(self.folder_path, 'r', encoding='utf-8') as file:
                lines = words = characters = 0
                for line in file:
                    lines += 1
                    words += len(line.split())
                    characters += len(line)
                return lines, words, characters
        except FileNotFoundError:
            print(f"File not found: {self.folder_path}")
            return 0, 0, 0
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return 0, 0, 0

    def get_text_stats(self):
        if self.folder_path.endswith(".txt") and os.path.isfile(self.folder_path):
            lines, words, characters = self.count_texts()
            return lines, words, characters
        else:
            print("Unsupported file format or file not found. Please provide a .txt file.")
            return 0, 0, 0

    def program_processing(self):
        valid_extensions = (".py", ".java", ".cpp", ".c")

        if self.folder_path.endswith(valid_extensions):
            if self.content is None:
                with open(self.folder_path, 'r', encoding='utf-8') as file:
                    self.content = file.read()


            lines = self.content.split('\n')
            line_count = len(lines)

            class_pattern = r'\bclass\b'
            class_count = len(re.findall(class_pattern, self.content))

            method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
            method_count = len(re.findall(method_pattern, self.content))

            words = self.content.split()
            word_count = len(words)

            char_count = len(self.content)

            return line_count, class_count, method_count, word_count, char_count

        return 0, 0, 0, 0, 0
