from shape_3d import Shape3d
from math import pi


class Cube(Shape3d):
    name = "Cube"

    def __init__(self, edge):
        self.edge = edge

    def surface_area(self):
        area = 6 * (self.edge ** 2)
        return area

    def volume(self):
        vol = self.edge ** 3
        return vol

