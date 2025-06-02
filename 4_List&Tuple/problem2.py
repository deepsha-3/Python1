# Write a program to accept marks os 6 students and display them in a sorted manner.

marks=[]

s1= int (input("Enter a students marks:"))
marks.append(s1)
s2= int (input("Enter a students marks:"))
marks.append(s2)
s3= int (input("Enter a students marks:"))
marks.append(s3)
s4= int (input("Enter a students marks:"))
marks.append(s4)
s5= int (input("Enter a students marks:"))
marks.append(s5)
s6= int (input("Enter a students marks:"))
marks.append(s6)

marks.sort()
print(marks) 



# we can use loop to run this program

marks = []    
for i in range(6):  
    mark = int(input(f"Enter marks for student {i+1}: "))  
    marks.append(mark)  

marks.sort()
print("Sorted marks:", marks)
