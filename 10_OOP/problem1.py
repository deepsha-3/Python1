# Create a Class "Programmer" for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, language, salary):
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary

programmer1 = Programmer("Rohit", 30, "Python", 80000)
print(f"Name: {programmer1.name}, Age: {programmer1.age}, Language: {programmer1.language}, Salary: {programmer1.salary}, Company: {programmer1.company}")

programmer2 = Programmer("Anjali", 28, "JavaScript", 75000)
print(f"Name: {programmer2.name}, Age: {programmer2.age}, Language: {programmer2.language}, Salary: {programmer2.salary}, Company: {programmer2.company}")

programmer3 = Programmer("Vikram", 35, "C#", 90000)
print(f"Name: {programmer3.name}, Age: {programmer3.age}, Language: {programmer3.language}, Salary: {programmer3.salary}, Company: {programmer3.company}")