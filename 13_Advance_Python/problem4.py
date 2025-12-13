
# write a program to display a/b where a and b are integers. If b = 0 display infinite by handling the 'ZeroDivisionError'.

try: 
    a = int (input("Enter numerator (a): "))
    b = int (input("Enter denominator (b): "))

except ValueError: