class Person:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print(f"Name: {self.name}")
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id
    def display_emp_info(self):
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, manager_id):
        super().__init__(name, emp_id)
        self.manager_id = manager_id
    def display_manager_info(self):
        print(f"Manager ID: {self.manager_id}")
manager = Manager("Guna", 123, 456)
manager.display_info() # Output: Name: Guna
manager.display_emp_info() # Output: Employee ID: 123
manager.display_manager_info()