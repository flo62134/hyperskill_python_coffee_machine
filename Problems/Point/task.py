from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        a = self.x - other_point.x
        b = self.y - other_point.y
        return sqrt((a * a) + (b * b))
