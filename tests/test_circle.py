import pytest
import math
import source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up method {method}")
        self.circle = shapes.Circle(2)

    def test_area(self):
        assert self.circle.area() == math.pi * 2 ** 2 # self.circle.radious

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * 2 # self.circle.radious