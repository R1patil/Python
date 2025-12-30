'''The json module in Python provides functions to work with JSON (JavaScript Object Notation) data. JSON is a 
lightweight data-interchange format widely used for data serialization and communication between a server and a 
web application, or between different components of an application. 
1. Serialization: It can convert Python data structures (like dictionaries and lists) into JSON strings using the 
json.dumps() function. 
2. Deserialization: It can parse JSON strings and convert them back into Python data structures using the 
json.loads() function. 
3. File I/O: It provides functions to read JSON data from a file and write JSON data to a file.'''
import json

FILE_NAME = "binarytext/users.json"

# -------- SAVE DATA --------
users = {
    "1": {"name": "Rahul", "age": 22, "city": "Bangalore"},
    "2": {"name": "Deathstroke", "age": 30, "city": "Acity"}
}

with open(FILE_NAME, "w") as file:
    json.dump(users, file, indent=4)

print("✅ User data saved to JSON file")

# -------- LOAD DATA --------
with open(FILE_NAME, "r") as file:
    loaded_users = json.load(file)

print("\n📂 Loaded Users:")
for uid, info in loaded_users.items():
    print(uid, "->", info)

print("\nType:", type(loaded_users))
