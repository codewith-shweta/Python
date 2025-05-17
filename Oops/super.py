class Shape:
    def __init__(self,color,filled):
        self.color =color
        self.filled = filled

    

class Circle(Shape):
    def __init__ (self,color,filled,radius):
        super().__init__(color, filled)
        self.radius = radius


class Square(Shape):
        def __init__ (self,color,filled,width):
            super().__init__(color,filled)
            self.width = width



class Triangle(Shape):
        def __init__ (self,color,filled,width,height):
            super().__init__(color,filled)
            self.width = width
            self.height = height

circle = Circle("red", "True", "5")
print(circle.filled)
print(circle.color)

triangle = Triangle("Black","False","10cm","5")
print(triangle.width)
print(f"{triangle.height}cm")
