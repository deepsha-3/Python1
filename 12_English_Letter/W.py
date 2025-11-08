
# Letter pattern W 

num = 7

for i in range(num):
    for j in range(num * 4 - 3): 
        if j == i or j == (num * 2 - 2 - i) or j == (num * 2 - 2 + i) or j == (num * 4 - 4 - i):
            print("*", end="")
        else:
            print(" ", end="")