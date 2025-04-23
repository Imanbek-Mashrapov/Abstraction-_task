from shape_3d import Shape3d
from math import pi


class Sphere(Shape3d):
    name = "Sphere"
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        area = 4 * pi * (self.radius ** 2)
        return area

    def volume(self):
        vol = (4/3) * pi * (self.radius ** 3)
        return vol

