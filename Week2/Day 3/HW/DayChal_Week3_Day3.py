import math
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None:
            raise ValueError("Valid")
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Valid")
    def area(self):
        return (self.radius**2) * math.pi
    def __str__(self):
       return f"radius is: {self.radius},diameter is: {self.diameter}"
    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        elif isinstance(other, int):
            new_radius = self.radius + other
            return Circle(radius=new_radius)
        else:
            raise TypeError("Valid")
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        elif isinstance(other,int):
            return self.radius > other
        else:
            raise TypeError("Valid")
    def __lt__(self,other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        elif isinstance(other,int):
            return self.radius < other
        else:
            raise TypeError("Valid")
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        elif isinstance(other,int):
            return self.radius == other
        else:
            raise TypeError("Valid")
circle1 = Circle(radius=10)
circle2 = Circle(radius=20)
print(circle1)
print(circle2)
circle3 = circle1 + circle1
print(circle1 > circle2)
print(circle1 == circle2)
print(circle1 > 6)
print(circle1 == 9)
circles = [circle1, circle2, Circle(radius=3), Circle(diameter=8)]
sorted_circles = sorted(circles, key=lambda c: c.radius)
print(sorted_circles)



        
