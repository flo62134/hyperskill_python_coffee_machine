import math
from math import sqrt


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        coefficient = (3 * sqrt(3)) / 2
        area = (self.side_length ** 2) * coefficient
        return round(area, 3)
