# write a program to find the sum of first n natural numbers using while loop.  
num= int(input("Enter the number:"))

a=1
sum=0
while(a<=num):
    sum+=a
    a+=1
print(sum)