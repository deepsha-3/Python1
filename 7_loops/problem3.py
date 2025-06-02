# write a program to print multiplication table of given number using for loop.

num= int(input("Enter the number:"))

for a in range(1,11):
    print(f"{num} X {a}={num*a}")
