# Write a program to calculate the factorial of a given number using for loop.
num= int(input("Enter the number:"))

product=1
for a in range(1, num+1):
    product=product*a

print(f"The factorial value of {num} is { product} ")