class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Comparing areas using < operator
if r1 < r2:
    print("Rectangle 1 has a smaller area")
else:
    print("Rectangle 2 has a smaller or equal area")
