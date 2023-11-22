class rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length*self.__breadth
    def perimeter(self):
        return 2*(self.__length+self.__breadth)
    def __it__(self,other):
        return self.area()< other.area()

rectangle1=rectangle(2,6)
rectangle2=rectangle(7,8)
area1=rectangle1.area()
area2=rectangle2.area()
print(area1)
print(area2)
if area1 < area2:
    print("area1 is larger than area2")
else:
    print("area2 is larger than area 1")
