# A file contians a word "Donkey" multiple times. You need to write a proram which replace this word with "#####" by updating the same file. 

#  donkey.txt is a file which contains the word "Donkey" multiple times.
word_to_replace = "Donkey"
with open("D:\\python\\9_FileIn_ot\\donkey.txt", "r") as file:
    content = file.read()
content= content.replace(word_to_replace, "#####")
with open("D:\\python\\9_FileIn_ot\\donkey.txt", "w") as file:
    file.write(content)
