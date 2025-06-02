# Write a program to find whether a given username contains less than 10 characters or not. 
user_name=input("Enter a username:")

if(len(user_name)<10):
    print("Username contains less then ten characters")
    
else:
    print("Your username is good.")