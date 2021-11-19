class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, a, b):
        print(f"Point{self.x},{self.y} {a} {b}")


point = Point(1, 2)
print(point.draw(1, 2))
