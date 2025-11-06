
# letter pattern T

num = 7

for i in range(num):
    for j in range(num):
        if i == 0 or j == num // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()