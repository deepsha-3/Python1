# Repeat program 4 for a list of such to be censored. 

# donkey2.txt is a file which contains the word "Donkey" "Monkey" and "day". 

words_to_replace= ["Donkey","Monkey", "day"]
with open("D:\\python\\9_FileIn_ot\\donkey2.txt", "r") as file:
    content = file.read()
    
for word in words_to_replace:
    content = content.replace(word, "#" * len(word))
with open("D:\\python\\9_FileIn_ot\\donkey2.txt", "w") as file:
    file.write(content)

