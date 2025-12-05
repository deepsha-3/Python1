
# enumerate function in Python

# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.

list = ['apple', 'banana', 'grapes', 'pear']

index = 0
for i in list:
    index += 1
    print(f"The item at index {index} is {i}")