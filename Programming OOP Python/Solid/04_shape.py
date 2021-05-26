from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def get_area(self):
        return self.side * self.height / 2


class AreaCalculator:
    def __init__(self, shapes):
        if isinstance(shapes, list):
            self.shapes = shapes
        else:
            print("`shapes` should be of type `list`.")

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()
        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
