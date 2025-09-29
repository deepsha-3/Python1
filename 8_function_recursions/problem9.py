# Write a python function to print multiplication table of given numbers.


def table(num):
    for a in range(1, 11):
        print(f"{num}X{a}={num*a}")


num=int(input("Enter the number:"))
table(num)