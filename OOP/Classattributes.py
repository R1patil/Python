# class attributes are variables that are shared among all instances of a class.
# They are defined within the class but outside any instance methods.   
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance 
        
    def info(self):
        return f"{self.name} is {self.age} years old."
    
# Creating instances of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
print(dog1.info())  # Output: Buddy is 3 years old.
print(dog2.info())  # Output: Lucy is 5 years old.  