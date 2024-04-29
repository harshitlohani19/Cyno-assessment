"""
importing classes from Geometry module
"""

from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle


"""
define main
"""


def main():
    """
    user input for shape
    """
    figure = input("Choose Shape: Circle, Rectangle, Square- ")
    figure = figure.lower()
    if figure == "circle":
        """
        input radius
        """
        radius = int(input("Enter Radius: "))
        circle = Circle(radius)
        print(Circle)
    elif figure == "square":
        """
        input length
        """
        length = int(input("Enter Length"))
        print(Square(length))
    elif figure == "rectangle":
        """
        input length and breadth
        """
        breadth, length = map(
            int, input("Enter Length and Breadth separated by space: ").split()
        )
        print(Rectangle(breadth, length))
    else:
        print("Invalid Shape")


main()
