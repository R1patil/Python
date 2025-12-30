'''a+ Mode: Opens the file for both reading and writing. The file is created if it doesn't exist. The file pointer is 
placed at the end of the file for writing. 
• The file pointer can be moved for reading. '''
with open('textfile/example1.txt', 'a+') as file: 
    file.write('\nAppending this line.') 
    file.seek(0) 
    print("Content after appending:", file.read()) 
 
# Appending more content 
with open('textfile/example1.txt', 'a+') as file: 
    file.write('\nAnother appended line.') 
    file.seek(0) 
    print("Content after second append:", file.read())