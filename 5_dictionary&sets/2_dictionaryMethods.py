#Dictionary Methods 


marks={ "Dipisha": 98,
        "Nikita": 69,
        "Deekshya":70,
        90: "Karan"
    }

print(marks.items()) # .items method
print(marks.keys())  # .keys method (left side keys)
print(marks.values())   # .values method( right side values)

marks.update({"Dipisha": 66, "Durga":90})
print(marks)  # .update method, which update that the key values pairs are avaible in the dictionary and which are not there that will be added 

print(marks.get("Kushum"))
print(marks.get("Dipisha"))
print(marks["Dipisha"])     # get method 



# The condition where get none and error 
print(marks.get("Dipisha1")) # print none
print(marks["Dipisha1"])   # Returns key error





