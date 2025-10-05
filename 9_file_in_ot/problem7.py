# write a program to find out the line number where python is present from questions 6.


with open("D:\\python\\9_FileIn_ot\\logfile.txt", "r") as file:
    content = file.read()

line_num=1
found=False
for line in content.splitlines():
    if "python" in line.lower():
        print(f"Python is available in logfile.txt. Line number: {line_num}")
        found=True
        break
    line_num +=1

if not found:
    print("Python is not available in logfile.txt.")