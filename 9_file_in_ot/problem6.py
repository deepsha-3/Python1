# Write a program to mine a log file and find out whether it contains 'python'.


with open("D:\\python\\9_FileIn_ot\\logfile.txt", "r") as file:
    content = file.read()


if ("python" in content):
        print("Python is available in logfile.txt.")
    
else:
        print("Python is not available in logfile.txt.")