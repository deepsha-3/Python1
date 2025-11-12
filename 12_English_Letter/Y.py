
# letter Partten Y

n = 7

for i in range(n):
    for j in range(n * 2 - 1):
        if j == n // 2:
            print("*", end="")
        elif i >= n // 2 and (j == i - n // 2 or j == (n * 2 - 2 - (i - n // 2))):
            print("*", end="")
            
        