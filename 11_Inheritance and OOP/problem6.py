
# Write __str__() method to print the vector as follows:
      # 7i + 8j + 9k

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b, self.c + other.c)
    
    def __mul__(self, other):
        return self.a * other.a + self.b * other.b + self.c * other.c
    
    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)        # 1i + 2j + 3k
print(v2)        # 4i + 5j + 6k
print(v1 + v2)   # 5i + 7j + 9k
print(v1 * v2)   # 32
