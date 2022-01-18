from Viewer3D import Plane, Point3D, Viewer3D
from math import sin, cos, pi


class OutOfPoints(Exception):
    pass


class Cone:

    def __init__(self, starting_point: Point3D, radius: int, height: int, points: int, rounds: int, offset: int = 0) -> None:
        self.starting_point = starting_point
        self.radius = radius
        self.points = points
        # Offsets per point
        self.offset = offset
        self.rad_offset_point = 2 * pi * rounds / points
        self.height_offset_point = height / points
        self.point = 0

    def nextPoint(self) -> Point3D:
        if self.point >= self.points:
            raise OutOfPoints()
        pt = Point3D(
            self.starting_point.x + round(sin(self.rad_offset_point * self.point + self.offset) *
                                          self.radius * ((self.points - self.point) / self.points), 0),
            self.starting_point.y + self.height_offset_point * self.point,
            self.starting_point.z + round(cos(self.rad_offset_point * self.point + self.offset) *
                                          self.radius * ((self.points - self.point) / self.points), 0),
        )
        self.point += 1
        return pt


if __name__ == "__main__":
    v = Viewer3D(Point3D(0, 50, 0), Plane(Point3D(70, 0, -40), 100, 80))

    def c_list(v: Viewer3D, c: Cone):
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
    print("<style>path:nth-child(1){d:path('"+s_1.replace("L", "M", 1)+"');}")
    print("path:nth-child(2){d:path('" + s_2.replace("L", "M", 1) + "');}")
    print("path{stroke-linecap:round;animation: a 2s linear 0s infinite forwards;stroke-dasharray: 4 4;fill: none;stroke-width:1px}@keyframes a {to{stroke-dashoffset:-8;}}</style>")
    print('<svg width="80" height="100"><path stroke="cyan"/><path stroke="red"/></svg>')
