with open("ErrorHandling/example.txt", "r") as file: 
    lines = file.readlines() 
    word_count = sum(len(line.split()) for line in lines) 
    print("Word count:", word_count) 


print("working with encoding")
    # Working with encodings 
with open("ErrorHandling/example.txt", "r", encoding="utf-8") as file: 
    file_contents = file.read() 
    print("File contents:", file_contents)