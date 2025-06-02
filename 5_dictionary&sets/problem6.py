# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names.Assume that the names are unique.

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