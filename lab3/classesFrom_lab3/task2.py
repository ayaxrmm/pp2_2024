'''Define a class named Shape and its subclass Square. The Square class
 has an init function which takes a length as argument. Both classes have 
 a area function which can print the area of the shape where Shape's area 
 is 0 by default.'''

class Shape :
    def __init__(self) :
        pass
    def area(self):
        return 0
class square(Shape) :
    def __init__(self, length):
        self.length=length
    def area(self):
        return self.length ** 2
Shape = Shape()
print("area of shape: " , Shape.area())
square = square(3)
print("area of square: ", square.area())

        