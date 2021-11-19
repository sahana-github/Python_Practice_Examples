class Point:
    def draw(self):
        print("draw")

    def line(self):
        print("line")

    def triangle(self):
        return "triangle"


point = Point()
point
print(point.triangle())
print(point.line())
print(point.draw())
