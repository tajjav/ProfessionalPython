from pathlib import Path

# create a path obj for the file
file_path = Path('example.txt')

# Open the file using the path obj
with file_path.open('r') as file:
    print(file.read())

