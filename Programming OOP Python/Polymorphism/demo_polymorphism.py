from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * pi ** 2

    def perimeter(self):
        return self.radius * 2 * pi


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


def print_shape(s: Shape):
    print(f'per {s.perimeter()}')
    print(f'area {s.area()}')


print_shape(Circle(3))
print_shape(Square(3))
