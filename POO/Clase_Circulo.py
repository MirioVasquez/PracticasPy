#Import math to work with __π
import math

#Classes
class Shape:
    pass

#Class Circle, uses radius and circumference as variables, has __π as a constant, deduct diameter and area
class Circle(Shape):
    __π = math.pi
    def __init__(self, radius=None, circumference=None,):
        if radius is not None:
            self.radius = radius
            self.circumference = 2*Circle.__π*radius
        elif circumference is not None:
            self.circumference = circumference
            self.radius = circumference/(2*Circle.__π)
        else:
            raise ValueError("You must provide either radius or circumference")
    
    #Methods of Circle
    def __diameter(self):
        return float(2*self.radius)
    def area(self):
        return float(Circle.__π*(self.radius**2))
    def get_pi(self):
        return self.__π
    def display_info(self):
        print(f"Radius: {self.radius:.4f}")
        print(f"Diameter: {self.__diameter():.4f}")
        print(f"Circumference: {self.circumference:.4f}")
        print(f"Area: {self.area():.4f}")
        print(f"Constant: {self.circumference/self.__diameter():.4f}")

#Class Pizza, inherit from Circle, add toppings variable, deduct the same as Cicle and the size of the pizza
class Pizza(Circle):
    def __init__(self, toppings ,radius=None, circumference=None):
        super().__init__(radius, circumference)
        self.toppings = toppings
        
    def big(self):
        if self.area() > 150:
            print(f"your {self.toppings} pizz is a larger one")
        else:
            if self.area() < 150:
                print(f"your {self.toppings} pizza is a personal one")

# # It is possible to change the value of '__π' from outside the class?
circle1 = Circle(None,4)
print(circle1.get_pi())
circle1.display_info()