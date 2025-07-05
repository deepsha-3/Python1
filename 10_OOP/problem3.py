# Create a class with a class attribute a; create an objec from it and set 'a' directly using object.a=o. Does this change the class attribute?

class Program:
    a = 1

o = Program()
print(o.a)  # class attribute print first because there is not instance attribute. 

o.a = 0  # create an instance attribute.
print(o.a) # print instance attribute. 

print(Program.a )  # print class attribute

# The class attribute is not change. 
 