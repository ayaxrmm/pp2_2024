import math
def areaofpoly(sides, length):
    apothem=length/(2*math.tan(math.pi/sides))
    perimetr=sides*length
    area=int(0.5*perimetr*apothem)
    return area
sides=int(input("enter a number of sides: "))
length=int(input("enter a length of 1 side: "))
print(areaofpoly(sides, length))
