# If the names of 2 friends are same; what will happen to the program in proble 6?
a={}
name= input("Enter first friends name:")
language= input("Enter your favorite language:")
a.update({name: language})

name= input("Enter second friends name:")
language= input("Enter your favorite language:")
a.update({name: language})

name= input("Enter third friends name:")
language= input("Enter your favorite language:")
a.update({name: language})

name= input("Enter fourth friends name:")
language= input("Enter your favorite language:")
a.update({name: language})

print(a)

# when two name are same then print the name which is entered in last time.

# we enter a same name it update automatically because of upate method.