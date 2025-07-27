# class() method in python:
# The class() function is used to create a new class dynamically.
 
class Programer:
    d = "Python"  # class attribute

    @classmethod
    def show(p):   # p is the class itself 
        print(f"The programming language is  {p.d }.")

language = Programer() 
language.d = "Java"   # changing class attribute "Pthon" to "Java"
language.show()  # method call