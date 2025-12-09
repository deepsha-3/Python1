
# Write a program to open three files 1.txt, 2.txt, and 3.txt if any these files are not present, a message without existing the program must be printed prompting the same. 

with open("1.txt", "r") as f:
    print(f.read())

with open("2.txt", "r"):