# Wite a python program to rename a file to "renamed_by_python.txt".

with open("D:\\python\\9_FileIn_ot\\thisnew.txt", "r") as file:
    content = file.read()   

with open("D:\\python\\9_FileIn_ot\\renamed_by_python.txt", "w") as file:
    file.write(content)

   