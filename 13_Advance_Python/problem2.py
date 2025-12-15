
# Write a program to print third, fifth and seventh element from a list using enumerate function.

list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
       # here 30 is 3rd element, 50 is 5th element and 70 is 7th element

for index, value in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        print(f"The element at index {index} is {value}")

        # Reminder: enumerate checks the index not the element itself