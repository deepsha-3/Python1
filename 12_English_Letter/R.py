
# letter pattern R

num = 7

for i in range(num):
    for j in range(num):
        if (j == 0) or (i == 0 and j < 4) or (i == 3 and j < 4) or (j == 4 and i != 0 and i < 3) or (i - j == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()