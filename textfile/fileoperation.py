# Readig the entire contents of the file as a string 

file_object = open("textfile/demo.txt","r")
r = file_object.read()
print(r)
file_object.close()

print("---------------------------")

# Read and return the next line from the file

file_object = open("textfile/demo.txt","r")
r = file_object.readline()
print(r)
file_object.close()

print("------------------------------")

#Read the return the a list of lines from the file

file_object = open("textfile/demo.txt","r")
r = file_object.readlines()
print(r)
file_object.close()

print("******************************")

# write the specified string to the file
file_object = open("textfile/demo.txt","w")
r = file_object.write("date is 12/28/25")
print(r)
file_object.close()

print("its demo of writing the file in the text")
#write the list of the lisdt of linesto the file
file_object = open("textfile/demo.txt","w")
r = file_object.writelines(["date is 12/28/25\n","tomarrow is the 29 date\n","we want finsh the tyoday only\n"])
print(r)
file_object.close()

''''
print("its the flushes internal buffers")
file_object = open("textfile/demo.txt","w")
r = file_object.flush()
print(r)
file_object.close() '''

# Moves the file pointer to a specified position
file_object = open("textfile/demo.txt","w")
r = file_object.seek(2,0)
print(r)
file_object.close()




