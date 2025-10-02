# Write a program to read the text from givien file 'poems.txt' and find out whether it constains the word 'twinkle'. 

f = open("D:\\python\\9_FileIn_ot\\poems.txt", 'r')
text= f.read()
if("twinkle" in text):
    print(" Oh yes, The word 'twinkle' is present in the poems.txt file.")
else:
    print(" Oh no, The word 'twinkle' is not present in the poems.txt file.")
f.close()