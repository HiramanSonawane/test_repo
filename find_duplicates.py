"""
     Logical Flow:
        - Set variables for file paths
        - Validate if files are present
        - Read first file into set 1
        - Read second file into set 2
        - Use intersection method to find intersection of set 1 and set 2 and store it into set 3
        - display set 3
"""
import os


def validate_file(file_name):
    return os.path.exists(file_name)


first_file = "a.txt"
second_file = "b.txt"

if not validate_file(first_file) or not validate_file(second_file):
    print("ERROR: Either file is not valid")
    exit(-1)

first_file_contents = set()
second_file_contents = set()

with open(first_file, 'r') as file1:
    first_file_contents.add(file1.readlines())

with open(second_file, 'r') as file2:
    second_file_contents.add(file2.readlines())

first_object = first_file_contents
second_object = second_file_contents

if len(first_file_contents) >= len(second_file_contents):
    first_object = second_file_contents
    second_object = first_file_contents

duplicate_lines = first_object.intersection(second_object)

if duplicate_lines:
    print(duplicate_lines)
else:
    print("No duplicate lines")
