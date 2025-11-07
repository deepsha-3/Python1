
# letter pattern V 

num = 7

for i in range(num):
    for j in range(num):
        if (j == i and i < num // 2) or (j == num - i - 1 and i < num // 2) or (i - j == num // 2 and i >= num // 2) or (i + j == num + (num // 2) - 1 and i >= num // 2):
            print("*", end="")
        else: