
# global variable in python

p = 1 # global variable

def func():
    global p  # using global keyword to modify the global variable

    p = p + 5
    print("Inside function:", p)

func()
print("Outside function:", p)