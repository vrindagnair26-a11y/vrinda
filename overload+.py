class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __add__(self, other):
        if self.area() > other.area():
            return "First rectangle has a larger area"
        elif self.area() < other.area():
            return "Second rectangle has a larger area"
        else:
            return "Both rectangles have equal area"


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Overloading + operator to compare areas
print(r1 + r2)