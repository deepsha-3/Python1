# Write a program to print the following star pattern.  (for n=3)
'''
   *
  ***
*****
'''  # This is a series of odd numbers
num= int(input("Enter the number:"))

for a in range(1, num+1):
    print(" "*(num-a), end="")  # end="" it will not give a by default newline
    print("*"* (2*a-1), end="")
    print("")     #  Moves to the next line

