
# creating the letter 'J' pattern

num = 7
for i in range(num):
    for p in range(num):
        if (i == 0) or (p == num // 2 and i != num -1 ) or (i == num -1 and p <= num // 2) :
           print("*", end=" ")