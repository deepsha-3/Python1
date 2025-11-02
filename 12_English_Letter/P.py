
# letter P pattern

num = 7
for i in range(num):
    for j in range(num):
        if (j == 0) or (i == 0 and j != num - 1) or (i == num // 2 and j != num - 1) or (j == num - 1 and i != 0 and i < num // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()