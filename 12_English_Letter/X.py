
# letter Partten X

n = 7 

for i in range(n):
    for j in range(n * 2 - 1):
      if j == i or j == (n * 2 - 2 - i):
            print("*", end="")