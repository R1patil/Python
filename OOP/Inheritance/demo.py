class Vechicle:
    def drive(self):
        return "Vechicle is driving"
    
class Car(Vechicle):
    def accelerate(self):
        return "Car is accelerating"
    
my_car = Car()
print(my_car.drive())        # Output: Vechicle is driving
print(my_car.accelerate())   # Output: Car is accelerating
print(issubclass(Car, Vechicle))  # Output: True