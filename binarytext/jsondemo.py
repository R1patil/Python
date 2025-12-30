import json 
# Data to work with 
data = {'name': 'John', 'age': 30, 'city': 'New York'} 
# Writing JSON data to a file 
with open('binarytext/data.json', 'w') as file: 
    json.dump(data, file) 
# Reading JSON data from a file 
with open('binarytext/data.json', 'r') as file: 
    loaded_data = json.load(file) 
# Working with loaded JSON data 
print("Loaded JSON data:", loaded_data) 
print("Name:", loaded_data['name']) 
print("Age:", loaded_data['age']) 
print("City:", loaded_data['city']) 
# Modifying data 
loaded_data['age'] = 31 
loaded_data['city'] = 'San Francisco' 
# Adding new key-value pair 
loaded_data['job'] = 'Engineer' 
# Writing modified JSON data back to file 
with open('data.json', 'w') as file: 
    json.dump(loaded_data, file) 
# Reading the modified JSON data from file 
with open('data.json', 'r') as file: 
    modified_data = json.load(file) 
print("Modified JSON data:", modified_data)