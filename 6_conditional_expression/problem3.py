# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 



# Three input fro the users
marks1=int(input("Enter first your marks: "))
marks2=int(input("Enter second your marks: "))
marks3=int(input("Enter third your marks: "))
   
   # Check for total percentage
total_percentage= (100*(marks1+ marks2+marks3))/300

# Using conditional expression 
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("You are pass.", total_percentage)

else:
    print("You are failled.", total_percentage)

