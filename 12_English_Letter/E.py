
# creating the letter 'E' pattern

n = 7 

for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n // 2 or i == n - 1:
            print("*", end=" ")
        else: