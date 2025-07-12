# single inheritance in python:
    # one child class inherits from one parent class.
class Person:
    def speak(self):   # parent class
        print("Can you speak.")

class Student(Person):  # child class
    def learn(self):
        print("Let's learn togther.")

s = Student()  # object create

# access parent and child methods
s.speak()   
s.learn()  
