"""
===========================================
PYTHON TUTORIAL: Strings and File Handling
===========================================
This file covers string manipulation and file operations.
Run this file with: python3 04_strings_file_handling.py
"""

print("=" * 60)
print("PART 1: STRING MANIPULATION")
print("=" * 60)

# String indexing (starts at 0, negative for reverse)
text = "Python"
print(f"\nString: {text}")
print(f"text[0] = {text[0]}, text[-1] = {text[-1]}")

# String slicing: [start:end:step]
print(f"\nSlicing: text[0:3]={text[0:3]}, text[:3]={text[:3]}, text[2:]={text[2:]}")
print(f"text[::-1] = {text[::-1]}")  # Reverse

# Concatenation
first = "Hello"
last = "World"
full = first + " " + last
print(f"\nConcatenation: {full}")

# String formatting
name, age = "Bob", 25
print(f"\nFormatting:")
print(f"f-string: My name is {name} and I'm {age} years old")
print(".format(): My name is {} and I'm {} years old".format(name, age))


# Common string methods
text = "  Hello World  "
print(f"\nMethods: .upper()={text.upper()}, .strip()='{text.strip()}'")
print(f".replace('World', 'Python')='{text.replace('World', 'Python')}'")
print(f".split()={text.strip().split()}")

print("\n" + "=" * 60)
print("PART 2: FILE HANDLING")
print("=" * 60)

# Opening and reading files (using 'with' - automatically closes file)
sample_content = "Line 1\nLine 2\nLine 3"
with open("sample.txt", "w") as file:
    file.write(sample_content)

print("\nReading file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"Full content:\n{content}")

print("\nReading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# File modes: 'r'=read, 'w'=write, 'a'=append, 'x'=exclusive, 'b'=binary, '+'=read+write
print("\nFile modes (w=write, a=append, r=read):")
with open("example.txt", "w") as f:
    f.write("First line\n")
with open("example.txt", "a") as f:
    f.write("Second line\n")
with open("example.txt", "r") as f:
    print(f.read())

# Writing to files
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.writelines(["Line 2\n", "Line 3\n"])

# Exception handling for files
print("\nException handling:")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Handling gracefully.")

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Read {len(lines)} lines successfully")
except IOError as e:
    print(f"Error: {e}")

# File paths
import os
from pathlib import Path

print("\nWorking with file paths:")
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "sample.txt")
print(f"Current dir: {current_dir}")
print(f"File exists: {os.path.exists(file_path)}")
print(f"File name: {os.path.basename(file_path)}")

# Using pathlib (modern approach)
path = Path("sample.txt")
print(f"\npathlib: exists={path.exists()}, stem={path.stem}, suffix={path.suffix}")

# Practical example: log file
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE")
print("=" * 60)

log_entries = [
    "2024-01-01 10:00:00 - System started",
    "2024-01-01 10:05:00 - User logged in",
]

with open("app.log", "w") as log_file:
    for entry in log_entries:
        log_file.write(entry + "\n")

try:
    with open("app.log", "r") as log_file:
        for line in log_file:
            date = line[:10]  # Using slicing
            message = line[13:].strip()
            print(f"Date: {date}, Message: {message}")
except FileNotFoundError:
    print("Log file not found")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- String indexing: [0], [-1], slicing: [start:end:step]")
print("- Use f-strings for formatting")
print("- Always use 'with' statement for files")
print("- Handle exceptions (FileNotFoundError, IOError)")
print("- Use os.path or pathlib for file paths")
print("\nCleaning up temporary files...")

# Cleanup
for temp_file in ["sample.txt", "example.txt", "output.txt", "app.log"]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
