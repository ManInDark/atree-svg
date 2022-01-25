from Object import Object, OutOfPoints
from Viewer3D import Point3D, Viewer3D, Plane


class Line(Object):

    """
    Draws a line from a starting point to an end point with the other points in between.
    """

    def __init__(self, starting_point: Point3D, points: int, end_point: Point3D) -> None:
        super().__init__(starting_point, points)
        self.end_point = end_point
        self.__x_diff = (self.end_point.x - self.starting_point.x) / (self.points - 1)
        self.__y_diff = (self.end_point.y - self.starting_point.y) / (self.points - 1)
        self.__z_diff = (self.end_point.z - self.starting_point.z) / (self.points - 1)

    def nextPoint(self) -> Point3D:
        if self.point >= self.points:
            raise OutOfPoints()
        pt = Point3D(self.point * self.__x_diff + self.starting_point.x, self.point * self.__y_diff +
                     self.starting_point.y, self.point * self.__z_diff + self.starting_point.z)
        self.point += 1
        return pt


if __name__ == "__main__":
    def c_list(v: Viewer3D, c: Object):
        list = []
        while True:
            try:
                list.append(v.translatePoint(v.see(c.nextPoint())))
            except OutOfPoints:
                break
        return list
    list = c_list(Viewer3D(Point3D(0, 5, 5), Plane(Point3D(10, 0, 0), 10, 10)),
                  Line(Point3D(10, 10, 10), 8, Point3D(10, 0, 10)))
    s = ""
    for e in list:
        s += e.pathPrint("L") + " "
    print("<style>body{margin:0px;}path{stroke-linecap:round;fill: none;stroke-width:1px; d:path('" +
          s.replace("L", "M", 1)+"');}</style>")
    print('<svg viewBox="0 0 10 10" height="100vh"><path stroke="red"/></svg>')
