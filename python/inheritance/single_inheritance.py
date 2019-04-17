
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

    