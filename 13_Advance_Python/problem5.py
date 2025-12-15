
# Store the multiplication tables genereted in problem 3 in a file named Tables.txt.

num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
print(f"Multiplication table of {num}: {table}")

with open("Tables.txt", "w") as file:
    file.write(f"Multiplication table of {num}: {table}\n")