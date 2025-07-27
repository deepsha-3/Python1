# multiple inheritance in python:
     # A child class inherits from more than one parent class.

class Car:  # parent class 1
    def start(self):
        print("Car started")

class Bike:  # parent class 2
    def stop(self):
            print("Bike stopped")

class Vehicle(Car, Bike):  # child class from  both parents
    def run(self):
        print("Vehicle is running")


v = Vehicle()  # object creation
v.start()  # method call from Car class
v.stop()   # method call from Bike class
v.run()    # method call from Vehicle class
