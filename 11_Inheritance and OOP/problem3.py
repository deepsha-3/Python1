
# Create a class "Employee" and add salary and increment properties to it. 
""" """

# first way as an instant attribute
class Employee:
    pass

emp = Employee()
emp.salary = 50000
emp.increment = 1.5
print(f"Salary: {emp.salary}")
print(f"Increment: {emp.increment}")





# second way as a class attribute
class Employee:
    salary = 50000
    increment = 1.5

emp = Employee()
print(f"Salary: {emp.salary}")         
print(f"Increment: {emp.increment}")