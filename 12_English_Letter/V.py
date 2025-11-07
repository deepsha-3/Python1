
# letter pattern V 

num = 7

for i in range(num):
    for j in range(num * 2 - 1):  # wider grid to allow symmetry
        if j == i or j == (num * 2 - 2 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
