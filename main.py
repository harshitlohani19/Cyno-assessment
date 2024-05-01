from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle


def main():
    figure = input("Choose Shape: (Circle, Rectangle, Square): ")
    figure = figure.lower()
    figure = figure.strip()
    if figure == "circle":
        radius = input("Enter Radius: ")
        try:
            radius = float(radius)
<<<<<<< HEAD
            if radius > 0:
                circle = Circle(float(radius))
                print(circle)
            else:
                print("Radius cannot be negative")
=======
            circle = Circle(float(radius))
            print(circle)
>>>>>>> a4fe171 (')
        except ValueError:
            print("Invalid Radius")
    elif figure == "square":
        length = input("Enter Length: ")
        try:
            length = float(length)
            print(Square(length))
        except ValueError:
            print("Invalid Length")
    elif figure == "rectangle":
        width = input("Enter Width: ")
        height = input("Enter Height: ")
        try:
            width = float(width)
            height = float(height)
            print(Rectangle(width, height))
        except ValueError:
            print("Invalid Width or Height")

    else:
        print("Invalid Shape")


main()
