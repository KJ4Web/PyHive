# Base class
class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"Shape Name: {self.name}")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    def __display(self):
        print(f"Length: {self.__length}, Width: {self.__width}")

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def show_details(self):
        self.display_info()
        self.__display()

rectangle = Rectangle("Rectangle", 10, 5)
rectangle.show_details()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")