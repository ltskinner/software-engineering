# Classes

## When to use

Two schools of thought on this one:
1. Classes when global like variables are needed
2. Classes when you need methods to modify an object and its intert data. As opposed to a function that completes a task for arbitrary data type

Regardless, class are most valuable when leveraging the **stateful** behavior that object attributes allow

```python
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
```

## Data Model Usage

Here, classes can be used to represent any ADT and override __dunder__ methods

```python
""" 
https://www.youtube.com/watch?v=cKPlPJyQrt4 
"""

"""
Full Data Model documentation:
    https://docs.python.org/3/reference/datamodel.html
"""

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass


if __name__ == "__main__":

    p1 = Polynomial(1, 2, 3) #  x^2 + 2x + 3
    p2 = Polynomial(3, 4, 3) # 3x^2 + 4x + 3

    # repr()
    print(p1) # Polynomial(*(1, 2, 3))

    # +
    print(p1 + p2) # Polynomial(*(4, 6, 6))

    # len()
    print(len(p1)) # 3
```

## Inheritance

### Single Inheritance

```python

"""
https://realpython.com/python-super/
"""


class Rectangle:
    def __init__(self, length, width, **kwargs):
        print("__init__: Rectangle")
        self.length = length
        self.width = width
        #super().__init__(**kwargs) # Rectangle, Square works without this

    def area(self):
        print("--> rectangle.area()")
        return self.length * self.width

    def perimiter(self):
        print("--> rectangle.perimiter()")
        return 2*self.length + 2*self.width


# Declare a Square class that inherits from the Rectangle class
class Square(Rectangle):
    """
    Has top level access to:
        Rectangle.area()
        Rectangle.perimiter()
    """
    """ __init__ b/c modifying attribute width to be length, 
    copying one parameter """
    # Classes implentation example from site
    def __init__(self, length, **kwargs):
        print("__init__: Square")
        super().__init__(length=length, width=length, **kwargs)


# Notice no init defined here
class Cube(Square):
    """
    Has top level access to:
        Square.Rectangle.area()
        Square.Rectangle.perimiter()
    """
    """ No __init__ b/c no new attributes """
    def surface_area(self):
        print("--> cube.surface_area()")
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        print("--> cube.volume()")
        face_area = super().area()
        return face_area * self.length


if __name__ == "__main__":
    
    """
    # Works for both class declarations
    square = Square(4)
    print("square.area():", square.area())
    print("square.perimiter():", square.perimiter())
    """
    """
    rectangle = Rectangle(2, 4)
    print("rectangle.area():", rectangle.area())
    """
    
    # Notice passing arugment, despite no init
    print(Cube.__mro__)
    cube = Cube(3)
    print("cube.area():", cube.area()) # access Rectangle.area()
    print("cube.perimiter():", cube.perimiter()) # access Rectangle.perimiter()
    print("cube.surface_area():", cube.surface_area())
    print("cube.volume():", cube.volume())
```

### Multiple Inheritance

```python
"""
https://realpython.com/python-super/
"""

from single_inheritance import Square

# Equivalent to Rectangle
class Triangle:
    def __init__(self, base, height, **kwargs):
        print("__init__: Triangle")
        self.base = base
        self.height = height
        super().__init__(**kwargs)
    
    def tri_area(self):
        print("--> triangle.tri_area()")
        return 0.5 * self.base * self.height 


"""
# Order matters, the methods of the first superclass are looked at first
# Also, when multiple inheritance, the most super class of the first 
# superclasses must have super().__init__(**kwargs) so that 
# the next class is initialized.
class RightPyramid(Square, Triangle):
    mro = (Square, Rectangle, Triangle)
    if Rectangle does not have super().__init__(), Triangle wont be reached

class RightPyramid(Triangle, Square):
    mro = (Triangle, Square, Rectangle)
    if Triangle does not have super().__init__(), Square wont be reached
"""
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height, **kwargs):
        print("__init__: RightPyramid")
        self.base = base
        self.slant_height = slant_height
        # Adding here instead of defining new --> kwargs may not be None
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def surface_area(self):
        print("--> pyramid.surface_area()")
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area*4 + base_area

    def volume(self):
        print("--> pyramid.volume()")
        height = (self.slant_height**2 + self.base**2)**.4
        return self.slant_height**2 * height / 3
    

class RightDiamond(RightPyramid):
    """ No __init__ b/c no new attributes """
    def surface_area(self):
        print("--> diamond.surface_area()")
        base_area = super().area()
        return 2*super().surface_area() - 2*base_area
    
    def volume(self):
        print("--> diamond.volume()")
        return 2*super().volume()


if __name__ == "__main__":

    """
    triangle = Triangle(3, 2)
    print("triangle.tri_area():", triangle.tri_area())
    """

    
    print(RightPyramid.__mro__)
    pyramid = RightPyramid(2, 4)
    print("pyramid.surface_area():", pyramid.surface_area())
    print("pyramid.volume():", pyramid.volume())

    print(RightDiamond.__mro__)
    diamond = RightDiamond(2, 4)
    print("diamond.surface_area():", diamond.surface_area())
    print("diamond.volume():", diamond.volume())
```
