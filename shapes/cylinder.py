from shape_3d import Shape3d
from math import pi


class Cylinder(Shape3d):
    name = "Cylinder"

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        area = 2 * pi * self.radius * (self.radius + self.height)
        return area

    def volume(self):
        vol = pi * (self.radius ** 2) * self.height
        return vol

