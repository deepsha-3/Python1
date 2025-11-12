
# letter Partten Y

n = 10

for i in range(n):
    for j in range(n * 2 - 1):
        if i < n // 2 and (j == i or j == (n * 2 - 2 - i)):
            print("*", end="")
        elif i >= n // 2 and j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
