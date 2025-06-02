# Write a program to fill in a letter template given below  with name and date
letter = '''
    Dear <|Name|>, 
    You are selected!
    <|Data|> 
   ''' 

print(letter.replace("<|Name|>", "Levent").replace("<|Data|>", "20 June 2003")) 