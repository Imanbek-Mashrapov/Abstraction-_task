from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
import random


def create_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

    if type == 'Sphere':
        radius = random.uniform(1, 10)
        return Sphere(radius)
    elif shape_type == 'Cylinder':
        radius = random.uniform(1, 10)
        height = random.uniform(5, 20)
        return Cylinder(radius, height)
    else:  # Cube
        edge = random.uniform(1, 10)
        return Cube(edge)


shapes = [create_random_shape() for i in range(10)]

for i, shape in enumerate(shapes, 1):
    print(f"\n {i}. {shape.name}")
    print(f"Surface Area: {round(shape.surface_area(), 2)} square units")
    print(f"Volume: {round(shape.volume(), 2)} cubic units")
    if shape.name == 'Sphere':
        print(f"Radius: {shape.radius:.2f} units")
    elif shape.name == 'Cylinder':
        print(f"Radius: {shape.radius:.2f} units, Height: {shape.height:.2f} units")
    else:  # Cube
        print(f"Edge: {shape.edge:.2f} units")
    print("-" * 50)