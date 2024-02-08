import math
class myShape:
    def __init__(self, color="black", is_filled=True):
        self.color=color
        self.is_filled= is_filled
    def __str__(self):
        return "color: ", self.color, "is filled: ", self.is_filled
    def getarea(self):
        return 0
class rectangle(myShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=0, width=0):
        self.color = color
        self.is_filled = is_filled
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    def __str__(self):
        return f"Color: {self.color}, Is Filled: {self.is_filled}, X Top Left: {self.x_top_left}, Y Top Left: {self.y_top_left}, Length: {self.length}, Width: {self.width}"
    def getarea(self):
        return self.length*self.width
class Circle(myShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=0):
        self.color = color
        self.is_filled = is_filled
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def __str__(self):
        return f"Color: {self.color}, Is Filled: {self.is_filled}, X Center: {self.x_center}, Y Center: {self.y_center}, Radius: {self.radius}"

    def getArea(self):
        import math
        return math.pi * self.radius ** 2
def create_rectangle_from_input():
    color = input("Enter color: ")
    is_filled = input("Is filled? (True/False): ").lower() == "true"
    x_top_left = int(input("Enter X coordinate of top left corner: "))
    y_top_left = int(input("Enter Y coordinate of top left corner: "))
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    return rectangle(color, is_filled, x_top_left, y_top_left, length, width)


rectangle = create_rectangle_from_input()
print(rectangle)
print("Area:", rectangle.getarea())