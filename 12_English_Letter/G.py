
# creating the letter 'G' pattern

n = 7

for i in range(n):
    for j in range(n):
        if (j == 0 and i != 0 and i != n - 1) or (i == 0 and j != 0 and j != n - 1) or (i == n - 1 and j != 0 and j >= n // 2) or (j == n - 1 and i >= n // 2 and i != n - 1) or (i == n // 2 and j >= n // 2):
            print("*", end=" ")
        else: