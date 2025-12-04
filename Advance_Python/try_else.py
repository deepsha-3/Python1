
# try with else in python

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except Exception as e:
    print("An error occurred:", e)

else:
    print("The result is:", result)