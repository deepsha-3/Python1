
 # Letter pattern 'M'

num = 8 

for i in range(num):
    for j in range(num):
        if j == 0 or j == num -1 or (i == j and i<= num//2) or (i + j == num -1 and i <= num//2):
            print("*", end="")
        else: