
# Letter pattern 'K'

num = 6

for i in range(num):
    for j in range(num):
        if (j == 0) or (i + j == num // 2) or (i - j == num // 2):
            