# Can you change the self-parametet inside a class to something else (say "dee"). Try changing to slf or dee and see the effects. 
 
class Car:
   name = "BMW"
   color = "Black"
   model = "X6"

   def newCar(slf):
        print(f" Car: {slf.name}, Color: {slf.color}, Model: {slf.model}")

def CarCar(dee):
        print(f" Car: {dee.name}, Color: {dee.color}, Model: {dee.model}")  # It not change anything in code.


company = Car()
company.newCar()