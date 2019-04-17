
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

