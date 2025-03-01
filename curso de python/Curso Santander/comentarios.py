import math

class Circle:
    π = math.pi
    def __init__(self, radius=None, circumference=None):
        if radius is not None:
            self.radius = radius
            self.circumference = 2*Circle.π*radius
        elif circumference is not None:
            self.circumference = circumference
            self.radius = circumference/(2*Circle.π)
        else:
            raise ValueError("You must provide either radius or circumference")
    
    #Methods
    def diameter(self):
        return float(2*self.radius)
    def area(self):
        return float(Circle.π*(self.radius**2))
    
    def display_info(self):
        print(f"Radius: {self.radius:.4f}")
        print(f"Diameter: {self.diameter():.4f}")
        print(f"Circumference: {self.circumference:.4f}")
        print(f"Area: {self.area():.4f}")
        print(f"Constant: {self.circumference/self.diameter():.4f}")
        
circle1 = Circle(radius=8)
circle2 = Circle(circumference=37.68)
print(20*"-")
circle1.display_info()
print(20*"-")
circle2.display_info()
