from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle


def main():
    """user input for shape"""
    figure = input("Choose Shape: Circle, Rectangle, Square- ")
    figure = figure.lower()
    if figure == "circle":
        radius = str(input("Enter Radius: "))
        radius = int(radius, 16)
        circle = Circle(radius)
        print(circle)
    elif figure == "square":
        length = int(input("Enter Length"))
        print(Square(length))
    elif figure == "rectangle":
        breadth, length = map(
            int, input("Enter Length and Breadth separated by space: ").split()
        )
        print(Rectangle(breadth, length))
    else:
        print("Invalid Shape")


main()
