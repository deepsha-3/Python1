
# Create a class "pets" from class "Animal" and furthure create a class "Dog" from class "pets". Add a method "bark" to class "Dog". 


class Animal:
    pass

class Pets(Animal):
    pass 

class Dog(Pets):
    def bark(self):
        print("Dog is barking.")

dog1 = Dog()
dog1.bark()

     