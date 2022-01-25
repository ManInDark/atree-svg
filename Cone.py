from Object import Object, OutOfPoints
from Viewer3D import Plane, Point3D, Viewer3D
from math import sin, cos, pi


class Cone(Object):

    """
    Draws a line in circles around the cone from bottom to top.
    """

    def __init__(self, starting_point: Point3D, radius: int, height: int, points: int, rounds: int, offset: int = 0) -> None:
        super().__init__(starting_point, points)
        self.__radius = radius
        # Offsets per point
        self.__offset = offset
        self.__rad_offset_point = 2 * pi * rounds / points
        self.__height_offset_point = height / points

    def nextPoint(self) -> Point3D:
        if self.point >= self.points:
            raise OutOfPoints()
        pt = Point3D(
            self.starting_point.x + round(sin(self.__rad_offset_point * self.point + self.__offset) *
                                          self.__radius * ((self.points - self.point) / self.points), 0),
            self.starting_point.y + self.__height_offset_point * self.point,
            self.starting_point.z + round(cos(self.__rad_offset_point * self.point + self.__offset) *
                                          self.__radius * ((self.points - self.point) / self.points), 0),
        )
        self.point += 1
        return pt


if __name__ == "__main__":
    v = Viewer3D(Point3D(0, 50, 0), Plane(Point3D(70, 0, -40), 100, 80))

    def c_list(v: Viewer3D, c: Object):
        list = []
        while True:
            try:
                list.append(v.translatePoint(v.see(c.nextPoint())))
            except OutOfPoints:
                break
        return list
    list_1 = c_list(v, Cone(Point3D(100, 6, 0), 30, 100, 200, 4, offset=pi))
    list_2 = c_list(v, Cone(Point3D(100, 6, 0), 30, 100, 200, 4))
    s_1 = ''
    for e in list_1:
        s_1 += e.pathPrint("L") + " "
    s_2 = ''
    for e in list_2:
        s_2 += e.pathPrint("L") + " "
    print("<style>body{margin:0px;}  path:nth-child(1){d:path('"+s_1.replace("L", "M", 1)+"');}")
    print("path:nth-child(2){d:path('" + s_2.replace("L", "M", 1) + "');}")
    print("path{stroke-linecap:round;animation: a 2s linear 0s infinite forwards;stroke-dasharray: 4 4;fill: none;stroke-width:1px}@keyframes a {to{stroke-dashoffset:-8;}}</style>")
    print('<svg viewBox="0 0 80 100" height="100vh"><path stroke="cyan"/><path stroke="red"/></svg>')
