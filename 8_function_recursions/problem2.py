# Write a program using functions to find greatest of three numbers.

# input from user
def greatest(d, e, f):
    if(d > e and d > f):
        return d
    elif(e > d and e > f):
        return e
    elif(f > e and f > d):
        return f
    
d = int(input("Enter the first number: "))
e = int(input("Enter the second number: "))
f = int(input("Enter the third number: "))

print(greatest(d, e, f))



# provide input
def greatest(d, e, f):
    if(d > e and d > f):
        return d
    elif(e > d and e > f):
        return e
    elif(f > e and f > d):
        return f
    
d = 9
e = 6
f = 4

print(greatest(d, e, f))