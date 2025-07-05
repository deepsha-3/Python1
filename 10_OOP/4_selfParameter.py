# self parameter in python is a reference to the current instance of the class.
# It is used to access variables that belong to the class.

class Car:
   name = "BMW"
   color = "Black"
   model = "X6"

   def newCar(self):
        print(f" Car: {self.name}, Color: {self.color}, Model: {self.model}")

company = Car()
company.newCar()  # This will print the car details without using self parameter    "First way to call the method"

# Car.newCar(company)           "Second way to call the method using class name"