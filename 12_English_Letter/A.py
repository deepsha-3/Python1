
# creating the letter 'A' pattern

n = 4 

for i in range(n):
    for j in range(2 * n - 1):
        if j == n - i - 1 or j == n + i - 1:
            print("*", end="")
        elif i == n // 2 and n - i - 1 < j < n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
