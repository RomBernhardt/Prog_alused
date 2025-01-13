from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """Circle constructor."""
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """Square constructor."""
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, length: float, width: float):
        """Rectangle constructor."""
        super().__init__(color)
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"

    def get_area(self) -> float:
        return self.length * self.width


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        return sum(shape.get_area() for shape in self.shapes)

    def get_circles(self) -> list:
        """Return only circles."""
        return [shape for shape in self.shapes if isinstance(shape, Circle)]

    def get_squares(self) -> list:
        """Return only squares."""
        return [shape for shape in self.shapes if isinstance(shape, Square)]

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        return [shape for shape in self.shapes if isinstance(shape, Rectangle)]


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("gray", 10, 20)
    
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    
    print(paint.calculate_total_area())
    print(paint.get_circles())
    print(paint.get_squares())
    print(paint.get_rectangles())
