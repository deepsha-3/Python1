
# creating the letter 'B' pattern

n = 7  

for i in range(n):
    for j in range(n):
        if j == 0:
            print("*", end="")  
        elif (i == 0 or i == n // 2 or i == n - 1) and j < n - 1:
            print("*", end="")  
        elif (i < n // 2 or i > n // 2) and j == n - 1:
            print("*", end="")  
        else:
            print(" ", end="")
    print()





""" n= 5
for i in range(n,-1,-1):                      
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(i+1):
        print("*",end=" ")
    print() """