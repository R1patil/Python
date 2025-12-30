
'''import os 
# Print the current working directory 
print("Before change:", os.getcwd()) 
# Change the directory to /tmp 
os.chdir('D:/file handling/textfile') 
print("After change:", os.getcwd()) '''
"""import os
if not os.path.exists('Nested_Dir/Level_1/Level_2/Level_3'): 
    os.makedirs('Nested_Dir/Level_1/Level_2/Level_3') 
    print("Directory created")
"""
"""import os 
 
# Remove a single empty directory 
if os.path.exists('test_dir'): 
    os.rmdir('test_dir') 
    print("Single Directory removed") """
 
"""# Remove nested directories 
if os.path.exists('D:/file handling/Nested_Dir/Level_1/Level_2/Level_3'): 
    os.removedirs('D:/file handling/Nested_Dir/Level_1/Level_2/Level_3') 
    print("Directory created") """



import os
# List the contents of the current directory 
contents = os.listdir('D:/file handling') 
print("Directory Contents:", contents)