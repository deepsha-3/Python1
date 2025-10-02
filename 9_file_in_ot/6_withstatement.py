# with statement 

f=open(r"D:\python\9_FileIn_ot\file.txt")
print(f.read())
f.close()


# we can use with statement in following way.

with open(r"D:\python\9_FileIn_ot\file.txt") as f:
    print(f.read())

# in with statement we don't need to close the f.close.
