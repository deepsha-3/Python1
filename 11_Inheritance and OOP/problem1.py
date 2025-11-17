
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.   

class Vector2D:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def display(self):
        print(f"Vector2D: ({self.a}, {self.b})")
    
class Vector3D(Vector2D):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def display(self):
        print(f"Vector3D: ({self.a}, {self.b}, {self.c})")
    
obj1 = Vector2D(3, 4)
obj1.display()
obj2 = Vector3D(3, 4, 5)
obj2.display()



