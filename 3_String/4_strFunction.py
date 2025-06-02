# string function is a way to manipulate and work with strings in Python.

name = "Dipisha"
print(len(name))                   # Output: 7 (length of the string)
print(name.endswith("sha"))        # Output: True (checks if the string ends with "sha")
print(name.startswith("Di"))       # Output: True (checks if the string starts with "Di")
print(name.find("pi"))             # Output: 2 (finds the index of the first occurrence of "pi")
print(name.replace("Dip", "Dee"))  # Output: Deeisha (replaces "Dip" with "Dee")    
print(name.upper())                # Output: DIPISHA (converts the string to uppercase)
print(name.lower())                # Output: dipisha (converts the string to lowercase)   
print(name.capitalize())           # Output: Dipisha (capitalizes the first letter of the string)