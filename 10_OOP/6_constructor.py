# constructor in python:
       # A constructor is a special method that is automatically called when an instance (object) of a class is created.
# It is also known as the `__init__` method.

class Person:
    name = "Kapil Sharma"
    age = 60
    city = "Mumbai"
    country = "India"

    def __init__(self): #dunder method which is called when an object is created.    
             # '__statred and __end' is called dunder method. 
        print("This is a constructor method.")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}")

Person1= Person()  # this is object.
Person1.display() 


