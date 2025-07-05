# class and instance

class Car:
    wheels =4 # class attribute  
     # class attribute is shared by all instances of the class.
    def __init__(self, color, model, year):
        self.color = color 
        self.model = model
        self.year = year # instance attributes
        # unique characteristics of each individual object. 
       
car1 = Car("Black", "BMW", 2020)
car2 = Car("White", "Porsche", 2021)
# we can print the class and instance attributes 
print(f"{car1.color} {car1.model} {car1.year} {car1.wheels}")
print(car2.color, car2.model, car2.year, car2.wheels)

