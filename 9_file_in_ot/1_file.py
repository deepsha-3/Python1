# text file 

f = open(r"D:\python\9_FileIn_ot\file.txt") # opent is a buil-in function which helps in opening files. 
content = f.read()     # (r)read is used to reading our files 
print(content)
f.close()             # close is used to close our opened files 