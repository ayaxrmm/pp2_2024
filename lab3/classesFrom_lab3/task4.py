'''Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points'''
import math 
class point :
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("coordinates: ",(self.x, self.y))
    def move(self, newx, newy):
        self.x=newx
        self.y=newy
    def dist(self,point2):
        dx=self.x-point2.x
        dy=self.y-point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
point1=point(1,2)
pointt2 = point( 3, 4)
point1.show()
pointt2.show()
distance = point1.dist(pointt2)
print("distance between two points: ", distance)
point1.move(2,3)
pointt2.move(4,5)
point1.show()
pointt2.show()



        