from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle


def main() -> None:
    figure = input("Choose Shape- Circle, Rectangle, Square :").lower().strip()
    if figure == "circle":
        radius = input("Enter Radius: ")
        try:
            radius = float(radius)
            if radius > 0:
                circle = Circle(float(radius))
                print(circle)
            else:
                print("Radius cannot be negative")
        except ValueError:
            print("Invalid Radius")
    elif figure == "square":
        length = input("Enter Length: ")
        try:
            length = float(length)
            if length < 0:
                print("Length cannot be negative")
            else:
                print(Square(length))
        except ValueError:
            print("Invalid Length")
    elif figure == "rectangle":
        width = input("Enter Width: ")
        height = input("Enter Height: ")
        try:
            width = float(width)
            height = float(height)
            if width < 0 or height < 0:
                print("Width or height cannot be 0")
            else:
                print(Rectangle(width, height))
        except ValueError:
            print("Invalid Width or Height")

    else:
        print("Invalid Shape")


main()
