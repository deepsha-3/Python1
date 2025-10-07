# Write a program to make a copy of a text file "this.txt".

with open("D:\\python\\9_FileIn_ot\\this.txt", "r") as file:
    content=file.read()

with open("D:\\python\\9_FileIn_ot\\this_copy.txt", "w") as file:
    file.write(content)

