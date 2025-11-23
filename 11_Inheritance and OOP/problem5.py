
# Write a class vector representing a vector of n dimensions. overloaded the +  and * operator which calcuates the sum and the dot(.) product of them. 

from unittest import result


class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        result = Vector(self.a + other.a, self.b + other.b, self.c + other.c)
        return result
    
    def __mul__(self, other):
        result = self.a * other.a + self.b * other.b + self.c * other.c
        return result
    
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
    
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(7, 8, 9)

    print("Sum of v1 and v2:", v1 + v2)
    print("Dot product of v2 and v3:", v2 * v3)

    print(v1 + v3)
    print(v1 * v3)

    # u = Vector(5, 6, 7)