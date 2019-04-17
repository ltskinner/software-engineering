
""" https://realpython.com/python3-object-oriented-programming/ """


# Python3 Class definitions
class Dog3:
    pass


# Python2 Class defintions
class Dog2(object):
    pass



class Doggo:

    # Class attributes
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
