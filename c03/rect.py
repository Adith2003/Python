from shapes import rectangle,circle
from shapes.d_graphics import cuboid,sphere
length=int(input("enter the length"))
width=int(input("enter the  width"))
area=rectangle.area(length,width)
perimeter=rectangle.perimeter(length,width)
print(area)
print(perimeter)
radius=float(input("enter a radius"))
area=circle.area(radius)
perimeter=circle.perimeter(radius)
print(area)
print(perimeter)
length=int(input("enter the length"))
width=int(input("enter the width"))
height=int(input("enter the height"))
area=cuboid.area(length,width,height)
perimeter=cuboid.perimeter(length,width,height)
print(area)
print(perimeter)
radius=int(input("enter the radius of sphere"))
area=sphere.area(radius)
perimeter=sphere.perimeter(radius)
print(area)
print(perimeter)
