# In the case where multiple cases of if statement 

d= int(input("Enter your age:"))

# If statement no:1
if(d%2==0):              # If statement would have run independently.
    print("d is even.")

#end of If statement no:1


# If statement no:2 
if(d>=18): 
    print("Your are 18 years old.")

elif(d<0):
    print("You enter negative.")

else:
    print("you are below the 18 years old.")

#end of If statement no:2

print("Empty")