import os

file_path = os.path.abspath('my_first_file.txt')

try:
    os.remove(file_path)
except FileNotFoundError:
    print('File already deleted!')