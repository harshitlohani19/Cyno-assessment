class Square:
    
    # Method to initialize an object of square class with provided length
    def __init__(self, side_length):
        self.side_length = side_length
    
    # Method to return the area of the square
    def area(self):
        return self.side_length ** 2
    
    # Method to calculate the perimeter of the square
    def perimeter(self):
        return 4 * self.side_length
    
    # Method to return the string representation of the square including the length, area, and perimeter
    def __str__(self):
        return f"Square with side length {self.side_length}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    # Method to compare the area of current square with another square, return True if equal,return False otherwise. 
    def __eq__(self, other):
        return self.area() == other.area()
    
    # Method to compare area of current square with another square and return True if area of the current square is less than the area of the other square,return  False otherwise.
    def __lt__(self, other):
        return self.area() < other.area()