
# Write a class vector representing a vector of n dimensions. overloaded the +  and * operator which calcuates the sum and the dot(.) product of them. 

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        result = Vector(self.a + other.a, self.b + other.b, self.c + other.c)
        return result
    
    # def __mul__(self, other):
        # result = self.a * other.a + self.b * other.b + self.c * other.c
       #  return result