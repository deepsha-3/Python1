
# creating the letter 'D' pattern

n = 7

for i in range(n):
    for j in range(n):
        if j == 0:
            print("*", end="")  
        elif (i == 0 or i == n - 1) and j < n - 1:
            print("*", end="")  
        elif (i > 0 and i < n - 1) and j == n - 1:
            print("*", end="")  
        else:
            print(" ", end="")
  
  