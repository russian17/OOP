import os

def count_texts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = words = characters = 0
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)
            return lines, words, characters
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0, 0, 0
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return 0, 0, 0

# Function to count lines, words, and characters in a .txt file
def get_text_stats(file_path):
    if file_path.endswith(".txt") and os.path.isfile(file_path):
        lines, words, characters = count_texts(file_path)
        return lines, words, characters
    else:
        print("Unsupported file format or file not found. Please provide a .txt file.")
        return 0, 0, 0

# Example usage:
file_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test\test2.txt"
lines, words, characters = get_text_stats(file_path)
print(f"Line Count: {lines}, Word Count: {words}, Character Count: {characters}")
