class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
rectangle1=rectangle(2,3)
rectangle2=rectangle(3,6)
area1=rectangle1.area()
area2=rectangle2.area()
print(area1)
print(area2)
if area1>area2:
    print("area1 is larger than area2")
elif area2>area1:
    print("area2 is larger than area1")
else:
    print("both area of rectangle are same")
