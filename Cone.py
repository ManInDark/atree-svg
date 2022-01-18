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
    s = ''
    for e in list_1:
        s += e.pathPrint("L") + " "
    s += list_2[0].pathPrint("M") + " "
    for n in range(1, len(list_2)):
        s += list_2[n].pathPrint("L") + " "
    print("<style>\n  path {\n    d: path('" + s.replace("L", "M", 1) + "');\n    stroke-linecap: round;\n    animation: a 2s linear 0s infinite forwards;\n  }\n\n  @keyframes a {\n    to {\n      stroke-dashoffset: -8;\n    }\n  }\n</style>")
    print('<svg width="80" height="100">\n  <path stroke="green" stroke-width="1px" fill="none" stroke-dasharray="4 4" />\n</svg>')
    # Add second rotated line for two seperate lines
