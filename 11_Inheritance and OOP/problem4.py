
# Write a cclass "Complex" to represent complex numbers (real and imaginary parts), along with overloaded operators '+' and '*' which adds and multiplies them. 

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
       return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self): 


other = Complex(2, 3)
com = Complex(1, 4)
print("Addition:", com + other)  # Output: Addition: 3 + 7i