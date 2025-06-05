# recursion is a functions which call itself.  

def factorial(n):
    if n==0 or n==1:   # Base case: stops the recursion when a specific condition is met
        return 1   
    else:
        return n* factorial(n-1)  # Recursive case: function calls itself with a modified argument to progress toward the base case.   
print(factorial(3))



# input from user

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
d= int(input("Enter this number:"))
print(f"This is the factorial is: {factorial(d)}" )