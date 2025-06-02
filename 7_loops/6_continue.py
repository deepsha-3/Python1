# continue statement 

# in case of for loop 
for a in range(50):
    if(a==30):
        continue   # continue ststement is work for skip the loop (skip this iteration).
    print(a)



# in case of while loop 
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue  # Skips printing when a is 3
    print(a)
