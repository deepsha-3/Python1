
# letter Pattern Z

n = 7

for i in range(n):
    for j in range(n * 2 - 1):
        if i == 0 or i == n - 1:
            print("*", end="")
        elif j == n - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")