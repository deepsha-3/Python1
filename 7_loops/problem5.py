# # write a program to print multiplication table of given number using while loop.


num= int(input("Enter the number:"))

a=1
while(a<=10):
    print(f"{num} X {a}={num*a}")
    a+=1