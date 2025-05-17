#property = setter , deleter, getter methods 

class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    @property

    def width(self):
        return f"{self._width}cm"     #_ private access'[_]
    @property
    def height(self):
        return f"{self._height}"

    @width.setter
    def width(self,new_width):
        if new_width < 0:
            self._width = new_width

        else:
            print("Width mustbe zero")


    @width.deleter
    def width(self):
         del self._width
         print("Width has been eliminated ")

rectangle = Rectangle(40, 24)

del rectangle.width

#print(rectangle.height)
#print(rectangle.width)+*