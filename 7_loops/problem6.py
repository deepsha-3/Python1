# write a program to find whether a given number is prime or not.

num= int(input("Enter the number:"))

for a in range(2,num):
    if(num%a)==0:
        print("The number is not prime.")
        break
else:
    print("The number is prime.")
 

