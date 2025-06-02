# Write a program to print the following star pattern.  (for n=3)
'''
***
* *
***
'''

num= int(input("Enter the number:"))

for a in range(1, num+1):
    if(a==1 or a==num):
        print("*"*num,end="")

    else:
        print("*",end="") 
        print(" "*(num-2),end="")
        print("*",end="")
    print("")

