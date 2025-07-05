# static method in python:
    # static method is a method that belongs to the class rather than an instance of the class.

class Employee:
    id=0
    name= "Kapil Sharma"
    salary= 15000

    @staticmethod
    def display():
        print(f"Employee ID: {Employee.id}, Name: {Employee.name}, Salary: {Employee.salary}")# static method can be called without creating an instance of the class.
Employee.display()   # this print the employee details without creating an instance of the class.