class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second

o1 = Time(2, 40, 10)
o2 = Time(4, 20, 50)
result = o1 + o2
print("Sum of time:", result)
