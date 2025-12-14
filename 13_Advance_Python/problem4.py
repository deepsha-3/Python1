
# write a program to display a/b where a and b are integers. If b = 0 display infinite by handling the 'ZeroDivisionError'.

try: 
    a = int (input("Enter a first number (a): "))
    b = int (input("Enter second number (b): "))
    print("Result of a/b is:", a/b)

except ZeroDivisionError:
    print("infinite")