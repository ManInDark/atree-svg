from Viewer3D import Point3D
from math import sin, cos, tan, pi


class OutOfPoints(Exception):
    pass


class Cone:

    def __init__(self, starting_point: Point3D, radius: int, height: int, points: int, rounds: int) -> None:
        self.starting_point = starting_point
        self.radius = radius
        self.points = points
        # Offsets per point
        self.rad_offset_point = 2 * pi * rounds / points
        self.height_offset_point = height / points
        self.point = 0

    def nextPoint(self) -> Point3D:
        if self.point >= self.points:
            raise OutOfPoints()
        pt = Point3D(
            self.starting_point.x + round(sin(self.rad_offset_point * self.point) *
                                          self.radius * ((self.points - self.point) / self.points), 0),
            self.starting_point.y + self.height_offset_point * self.point,
            self.starting_point.z + round(cos(self.rad_offset_point * self.point) *
                                          self.radius * ((self.points - self.point) / self.points), 0),
        )
        self.point += 1
        return pt

if __name__ == "__main__":
    c = Cone(Point3D(0, 0, 0), 10, 8, 8, 2)
    ca = [c.nextPoint() for i in range(8)]
    for cap in ca:
        print(cap)