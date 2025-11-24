
# Override the __len__() method on vector of problem 5 (problem5.py) to display the dimension of the vector.

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
        return f"({self.a}, {self.b}, {self.c})"
    def __len__(self):
        return 3

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print("Sum of v1 and v2:", v1 + v2)
print("Dot product of v2 and v3:", v2 * v3)
print(v1 + v3)
print(v1 * v3)


print("Dimension of Vector v1:", len(v1))
print("Dimension of Vector v2:", len(v2))
print("Dimension of Vector v3:", len(v3))