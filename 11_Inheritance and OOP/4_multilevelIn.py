# multilevel inheritance in python:
   # A child class inherits from a parent class, which in turn inherits from another parent class.

class Vehicle:  # base parent class
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):  # intermediate child class
    def drive(self):
        print("Car is driving.")

class BMW(Car):  # derived child class
    def model(self):
        print("This is new BMW car.")

a = BMW()  # object creation
a.start()  # method from Vehicle class
a.drive()  # method from Car class
a.model()  # method from BMW class