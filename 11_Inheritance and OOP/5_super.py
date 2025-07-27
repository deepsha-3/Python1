# super() method in python:
     # The super() function is used to call a method from a parent class.

class Car:   # parent class
    def show(self):
        print("Showing car details.")

class Audi(Car):   # child class
    def show(self):
        super().show()
        print("Showing audi details.")

obj = Audi()   
obj.show()