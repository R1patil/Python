with open("demoseek.txt",'w') as file:
    r=file.write("Rahul was doing the python full stack course")
    print(r)

with open('demoseek.txt', 'r+') as file: 
    # reads the existing content and prints 
    print("Initial content:", file.read()) 
    file.seek(0)  # places the cursor in the beginning of the file 
    file.write('Hello, World!') 
    # This will overwrite the existing data 
 
# Reading the file again to see changes 
with open('demoseek.txt', 'r') as file: 
    print("Updated content:", file.read())