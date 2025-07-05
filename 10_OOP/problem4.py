# Add static method in problem2.py to greet the user with hello.

class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def square_root(self, num):
        return num ** 1/2
    
    @staticmethod
    def hello():
        pass

    
print("Hello, are you there.")
print("Calculator Operations:")
calc = Calculator()     
number = 4
print(f"Square of {number}: {calc.square(number)}")


print(f"Cube of {number}: {calc.cube(number)}") 
print(f"Square root of {number}: {calc.square_root(number)}")