# write a program  which finds out whether a given name is present in a list or not. 
list=["Dipisha", "Durga", "Deekshya", "Nikita","Kushum", "Kartik", "Karan" ]  

name=input("Enter your name:")  # If we enter a small letter in input it gives error because pyhton is case-sensitive. 
if(name in list):
    print("Your name is in the list.")

else:
    print("Your name is not in the list.")