from Object import Object, OutOfPoints
from Viewer3D import Point3D, Point2D, Viewer3D, Plane


class Line(Object):

    """
    Draws a line from a starting point to an end point with the other points in between.
    """

    def __init__(self, starting_point: Point3D, points: int, end_point: Point3D) -> None:
        super().__init__(starting_point, points)
        self.end_point = end_point
        self.starting_point = starting_point

    def nextPoint(self) -> Point3D:
        pt: Point3D = self.starting_point
        if self.point == 1:
            pt = self.end_point
        elif self.point > 1:
            raise OutOfPoints()
        self.point += 1
        return pt


if __name__ == "__main__":
    def c_list(v: Viewer3D, c: Object) -> list[Point2D]:
        list: list[Point2D] = []
        while True:
            try:
                list.append(v.translatePoint(v.see(c.nextPoint())))
            except OutOfPoints:
                break
        return list
    list = c_list(Viewer3D(Point3D(0, 5, 5), Plane(Point3D(10, 0, 0), 10, 10)),
                  Line(Point3D(10, 10, 10), 8, Point3D(10, 0, 10)))
    s = " ".join([e.pathPrint("L") for e in list])
    print("<style>body{margin:0px;}path{stroke-linecap:round;fill: none;stroke-width:1px; d:path('" +
          s.replace("L", "M", 1)+"');}</style>")
    print('<svg viewBox="0 0 10 10" height="100vh"><path stroke="red"/></svg>')
