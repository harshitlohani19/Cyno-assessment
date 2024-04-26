# Geometry Module

## Introduction
The Geometry Module is a Python package that provides services to compute and handle geometric figures: circles, squares, and rectangles. This module includes initializers, string representations, and comparison capabilities for each figure type. Additionally, a test script is provided to verify the functionality of these components. The project is hosted on GitHub and executable from the command line, with clear documentation and example snippets provided for users.

## Features
- Classes for representing circles, squares, and rectangles
- Methods for initializing, computing area/perimeter, and providing string representations
- Comparison methods to compare objects based on their area
- Test script using Python's unittest framework to ensure functionality

# Usage

```bash 
#from geometry import Circle, Square, Rectangle

# Create a circle with radius 5
circle = Circle(5)
print(circle)  # Output: Circle with radius 5
print("Area:", circle.area())  # Output: Area: 78.54

# Create a square with side length 4
square = Square(4)
print(square)  # Output: Square with side length 4
print("Area:", square.area())  # Output: Area: 16

# Create a rectangle with width 3 and height 4
rectangle = Rectangle(3, 4)
print(rectangle)  # Output: Rectangle with width 3 and height 4
print("Area:", rectangle.area())  # Output: Area: 12 
```
# Running Tests
```bash
python test_geometry.py
```
# Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

# License
This project is licensed under the [MIT License](LICENSE.md).