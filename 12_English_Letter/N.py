
# Letter pattern 'N'

num = 8

for i in range(num):
    for j in range(num):
        if j == 0 or j == num - 1 or i == j:
            print("*", end="")
        else:
            print(" ", end="")

    print()