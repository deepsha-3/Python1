# module that uses the pyjokes library

import pyjokes


# print("Hello from module.py!")
"""This is a simple module that uses the pyjokes
 library to get
   a random joke."""
joke = pyjokes.get_joke()
print(joke)