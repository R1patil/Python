class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)  # Inheriting attributes from Person
        self.employee_id = employee_id  # New attribute for Employee

    def display_employee(self):
        parent_info = Person.display_info(self)  # Calling method from Person
        return f"{parent_info}, Employee ID: {self.employee_id}"
    
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department):
        Person.__init__(self, name, age)  # Inheriting attributes from Person
        Employee.__init__(self, name, age, employee_id)  # Inheriting attributes from Employee
        self.department = department  # New attribute for Manager

    def display_manager(self):
        parent_info = Person.display_info(self)  # Calling method from Person
        employee_info = Employee.display_employee(self)  # Calling method from Employee
        return f"{employee_info}, Department: {self.department}"
    
manager1 = Manager("Bob", 35, "E123", "Sales")
print(manager1.display_manager())  # Output: Name: Bob, Age: 35, Employee ID: E123, Department: Sales