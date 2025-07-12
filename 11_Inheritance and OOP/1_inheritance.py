# inheritance in python 
class Computer:  # base\ parent class
    name = "Lenovo"  # default attribute
    def display(self):
        print(f"This is my computer {self.name}")
        
class Laptop(Computer):  # inherit\child class
    name = "Dell"    # attribute (overriding)
    def run(self):   
        pass

a = Computer()
b = Laptop()

print(a.name, b.name) 