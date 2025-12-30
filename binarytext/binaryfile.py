import pickle

# File name
FILE_NAME = "binarytext/users.pkl"

# --------- SAVE DATA ---------
users = {
    1: {"name": "Rahul", "age": 22, "city": "Bangalore"},
    2: {"name": "Deathstroke", "age": 30, "city": "Acity"}
}

with open(FILE_NAME, "wb") as file:
    pickle.dump(users, file)

print("✅ User data saved successfully")

# --------- LOAD DATA ---------
with open(FILE_NAME, "rb") as file:
    loaded_users = pickle.load(file)

print("\n📂 Loaded Users:")
for uid, info in loaded_users.items():
    print(uid, "->", info)

print("\nType:", type(loaded_users))
