class Geometry:
    def circle(self, r):
        circle = 3.142*r*r
        #r = int(input("Enter the radius: "))
        print("Area Of Circle is:")
        print(circle)

    def triangle(self, b, h):
        triangle = (1/2)*b*h
        #b = int(input("Enter the base:"))
        #h = int(input("Enter the height:"))
        print("Area of triangle is:")
        print(triangle)

    def rectangle(self, l, b):
        rectangle = l*b
        #l = int(input("Enter the length:"))
        #b = int(input("Enter the breadth:"))
        print("Area of rectangle is:")
        print(rectangle)


geo = Geometry()
print(geo.circle(2))
print(geo.triangle(2, 4))
print(geo.rectangle(4, 5))
