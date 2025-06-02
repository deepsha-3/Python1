# Write a proogram to find the greatest of four numbers entered by the user.

d1= int(input("Enter the first number:"))  # input function output is always return in string so give the int { (type cast) from string to int}
d2= int(input("Enter the second number:"))
d3= int(input("Enter the third number:"))
d4= int(input("Enter the fourth number:"))

if(d1>d2 and d1>d3 and d1>d4):
    print("The first is greatest number:", d1)

elif(d2>d1 and d2>d3 and d2>d4):
    print("The second is greatest number:", d2)

elif(d3>d1 and d3>d2 and d3>d4):
    print("The third is greatest number:", d3)

elif(d4>d1 and d4>d2 and d4>d3):
    print("The fourth is greatest number:", d4)

else:
    print("You enter invalid number.")