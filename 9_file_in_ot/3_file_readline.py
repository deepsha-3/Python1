# file other function 
"""
open
read
write
readline
close
"""
f = open(r"D:\python\9_FileIn_ot\file.txt")
# line= f.readline()
# print(line, type(line))

line1=f.readline()
print(line1, type(line1))


line2=f.readline()
print(line2, type(line2))  # Line two is empty but it shows the <class 'str'> because readline() always returns string value(dt), even when line appears blank.

line3=f.readline()
print(line3, type(line3))


# line4=f.readline()
# print(line4, type(line4))

f.close()
