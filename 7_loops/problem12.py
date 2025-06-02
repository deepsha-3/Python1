# Write a program to print multiplication table of n using for loops in reversed order.


num= int(input("Enter the number:"))

for a in range(1,11):
    print(f"{num} X {11- a}={num*(11-a)}")
