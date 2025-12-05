# Q4. Create a class Shape with a mehod area().
# Create subclasses Circle, Rectangle, and Triangle that override the area() method.

class Shape:
    def area(self):
        print("Area not defined")

Pi = 3.14

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = Pi * (self.radius**2)
        return area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        return area



c1 = Circle(5)
print(c1.area())

R1 = Rectangle(5, 8)
print(R1.area())

T1 = Triangle(3, 5)
print(T1.area())