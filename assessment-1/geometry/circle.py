import math
class circle:
    def __init__(self,radius):#Method to intialize circle radius
        self.radius= radius
    
    def area(self):#Method to return Circle Area
        area = math.pi * self.radius**2
        return area

    def circumference(self): #Method to return Cicle Circumference
        circumference = 2*math.pi*self.radius
        return circumference
    
    def __str__(self):#Method to return string representation
         str = f"Circle radius: {self.radius}, Area: {self.area()}, Circumference: {self.circumference()}"
         return str
    def __eq__(self, other):#Method to check if areas are equal or not,returns True/False
        aeq = self.area() == other.area()
        return aeq     
    
    def __lt__(self,other):#Method to Check if area1 is < than area2,returns True/False
        lt = self.area() < other.area()
        return lt