class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Inheriting attributes from Person
        self.student_id = student_id  # New attribute for Student
    def display_student(self):
        parent_info = super().display_info()  # Calling method from Person
        return f"{parent_info}, Student ID: {self.student_id}"
    
employee1 = Student("Alice", 20, "S12345")
print(employee1.display_student())  # Output: Name: Alice, Age: 20, Student ID: S12345