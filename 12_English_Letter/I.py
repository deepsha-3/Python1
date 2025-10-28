
# creating the letter 'I' pattern

num = 7

for i in range(num):
    for j in range(num):
        if i == 0 or i == num -1 or j == num // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")