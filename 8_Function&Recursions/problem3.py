# Write a python program using function to convert Celsius to Fahrenheit. 
                 
def degree(f): 
    return 5*(f-32)/9
f=int(input("Enter the temperature in F:"))

# c/5=(f-32)/9  formula celsius to fahrenheit. 
a= degree(f)
print(f"{round(a,2)} degree C")
