class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = MyPoint(1, 2) #creates instance of class
point.draw()
#print(type(point))

#print(isinstance(point, MyPoint))