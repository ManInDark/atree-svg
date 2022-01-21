from Object import Object, OutOfPoints
from Viewer3D import Point3D


class Line(Object):

    """
    Draws a line from a starting point to an end point with the other points in between.
    """

    def __init__(self, starting_point: Point3D, points: int, end_point: Point3D) -> None:
        super().__init__(starting_point, points)
        self.end_point = end_point
        self.x_diff = (self.end_point.x - self.starting_point.x) / (self.points - 1)
        self.y_diff = (self.end_point.y - self.starting_point.y) / (self.points - 1)
        self.z_diff = (self.end_point.z - self.starting_point.z) / (self.points - 1)
        self.point = 0

    def nextPoint(self) -> Point3D:
        if self.point >= self.points:
            raise OutOfPoints()
        pt = Point3D(self.point * self.x_diff, self.point * self.y_diff, self.point * self.z_diff)
        self.point += 1
        return pt


if __name__ == "__main__":
    l = Line(Point3D(0, 0, 0), 11, Point3D(10, 10, 10))
    for i in range(11):
        print(l.nextPoint())
