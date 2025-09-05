# property decorators in python:
   # Property decorators are a way to manage the attributes of a class. They allow you to define methods in a class that can be accessed like attributes, providing a way to add validation or other logic when getting or setting a value.

class Car:
    model = "BMW X5"

    def __init__(self, model):
        self._model = model

    @property
    def model(self):
         """Get the model of the car."""
         return self._model

obj = Car("")
obj.model
print(obj.model)