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