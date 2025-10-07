# Write a program to find out whether a file is identical and matches the content of another file. 

with open("D:\\python\\9_FileIn_ot\\this.txt") as file1:
    content1 = file1.read()

with open("D:\\python\\9_FileIn_ot\\this.txt") as file2:
    content2 = file2.read()

if content1== content2:
    print("The files are identical.")
else:
    print("The files are not identical.")