#w+ Mode: Opens the file for both reading and writing. The file is created if it doesn't exist. If the file exists, its 
#contents are truncated (i.e., deleted).
with open('textfile/example.txt', 'w+') as file: 
    file.write('Hello, World!') 
    file.seek(0) 
    print("Content after write:", file.read()) 
 
# Reopening to demonstrate truncation 
with open('textfile/example.txt', 'w+') as file: 
    print("Content before writing:", file.read()) 
    file.write('New Content') 
    file.seek(0) 
    print("Content after new write:", file.read())