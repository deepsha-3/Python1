
# Create a class "Employee" and add salary and increment properties to it. 
""" 
Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.   

"""

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
    increment = 40
    @property
    def salaryAfterIncrement(self):
        return (self.salary +self.salary * self.increment /100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100
       


emp = Employee()
# print(emp.salaryAfterIncrement)

emp.salaryAfterIncrement = 10