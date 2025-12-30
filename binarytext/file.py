import pickle


data={"name":"deathstroke","age":30,"city":"Acity"}
data1={"name":"rahul","age":32,"city":"ban"}

with open("data","wb") as file:
    pickle.dump(data,file)
    pickle.dump(data1,file)

with open("data","rb") as t:
    loaded_data=pickle.load(t)
    loaded_data1=pickle.load(t)

print(loaded_data)
print(loaded_data1)

print(type(loaded_data))
print(type(loaded_data1))