'''Error Handling: When working with files, it's important to handle potential errors, such as file not found or 
permission denied, gracefully. '''
# Iterating over lines in a file with exception handling 
file_path = "ErrorHandling/example.txt" 
 
try: 
    # Open the file 
    with open(file_path, "r") as file: 
        print("Iterating over lines in:", file_path) 
 
        # Read and print each line 
        line_number = 1 
        for line in file: 
            print(f"Line {line_number}: {line.strip()}")   
            # strip() removes the newline character at the end 
            line_number += 1 
 
except FileNotFoundError: 
    print(f"Error: File '{file_path}' not found.") 
 
except PermissionError: 
    print(f"Error: Permission denied to open '{file_path}'.") 
 
except Exception as e: 
    print(f"Error: {e}")