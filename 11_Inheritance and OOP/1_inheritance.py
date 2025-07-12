# inheritance in python 
class Computer:  # base\ parent class
    name = "Lenovo"  # default attribute
    def display(self):  # display method
        print(f"This is my computer {self.name}")
        
class Laptop(Computer):  # inherit\child class
    name = "Dell"    # attribute (overriding)
    def run(self):  # run method 
        pass

a = Computer()
b = Laptop()

print(a.name, b.name) 