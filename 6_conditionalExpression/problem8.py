# Write a program to find out whether a given post is talking about "Dipisha" or not. 


post ="Jaane bela ta hajurko bhok lai double boost garera pathaune ho, hai? Ramailo garera khau, ani feri chill garna aau! Bye bye, chef Dipisha! 😆👩‍🍳"


if("Dipisha" in post):
    print("This is talking about Dipisha.")

else:
    print("This post is not talking about Dipisha.")

 # we can run this program like this in this case we can give the captial and smmall post it can read and gives the output.

post= input("Enter the post:")

if("Dipisha".lower() in post.lower()):
      print("This is talking about Dipisha.")

else:
    print("This post is not talking about Dipisha.")
 