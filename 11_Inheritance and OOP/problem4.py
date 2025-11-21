
# Write a cclass "Complex" to represent complex numbers (real and imaginary parts), along with overloaded operators '+' and '*' which adds and multiplies them. 

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
       return Complex(self.real + other.real, self.imag + other.imag)
 
other = Complex(2, 3)
com = Complex(1, 4)