# Write a python function to remove a given word from a list ad strip it at the same time. 


def wordrem(list, wordremove):
    num = []
    for item in list:
        if not(item == wordremove):
            num.append(item.strip(wordremove))
    return num
      
list=["Apple", "Ball", "Append","App" "Dog" ]
print(wordrem(list, "App"))

