# 1. Write a program to print yes when the age entered by the user is greater than or equal to 18.

age=int(input("Enter your age:"))

if(age>=18):
    print("Yes")

elif(age>0):
    print("No")

else:
    print("You enter the valid age.")
