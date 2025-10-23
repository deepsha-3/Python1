# Creating the letter 'C' pattern

n = 7

for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1) and j > 0:  # Top and bottom 
            print("*", end="")
        elif (i > 0 and i < n - 1) and j == 0:  
            print("*", end="")
        else:
            print(" ", end="")
    print()