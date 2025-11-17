
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.   

class Vector2D:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
class Vector3D:
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    
