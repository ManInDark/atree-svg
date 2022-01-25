class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def pathPrint(self, prefix: str) -> str:
        return f"{prefix} {self.x}, {self.y}"


class Point3D(Point2D):
    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y)
        self.z = z

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


class Plane:
    def __init__(self, p: Point3D, y_dimension: int, z_dimension: int) -> None:
        self.point = p
        self.width = z_dimension
        self.height = y_dimension

    def translatePoint(self, p: Point2D) -> Point2D:
        return Point2D(abs(p.x - self.width), abs(p.y - self.height))

    def __str__(self) -> str:
        return f"{self.point}, width: {self.width}, height: {self.height}"

    def __repr__(self) -> str:
        return f"{self.point}, width: {self.width}, height: {self.height}"


class OutOfView(Exception):
    def __init__(self, direction: str, location: int, range: str, *args: object) -> None:
        super().__init__(*args)
        self.direction = direction
        self.location = location
        self.range = range

    def __str__(self) -> str:
        return f"Point didn't fit in {self.direction}-direction: {self.location} out of {self.range}"

    def __repr__(self) -> str:
        return f"Point didn't fit in {self.direction}-direction: {self.location} out of {self.range}"


class Viewer3D:

    def __init__(self, eye: Point3D, drawingplane: Plane):
        self.eye = eye
        self.plane = drawingplane
        self.eye_plane_distance = drawingplane.point.x - eye.x

    def see(self, p: Point3D) -> Point2D:
        try:
            my = (self.eye.y - p.y) / (self.eye.x - p.x)
            mz = (self.eye.z - p.z) / (self.eye.x - p.x)
            y = self.eye.y + my * self.eye_plane_distance - self.plane.point.y
            if not (y >= 0 and y <= self.plane.height):
                raise OutOfView("y", y, f"{0}..{self.plane.height}")
            z = self.eye.z + mz * self.eye_plane_distance - self.plane.point.z
            if not (z >= 0 and z <= self.plane.width):
                raise OutOfView("z", z, f"{0}..{self.plane.width}")
            return Point2D(z, y)
        except ZeroDivisionError:
            raise OutOfView("x", 0, "0..∞")

    def translatePoint(self, p: Point2D) -> Point2D:
        return self.plane.translatePoint(p)

    def __str__(self) -> str:
        return f"eye: ({self.eye}), plane: ({self.plane})"

    def __repr__(self) -> str:
        return f"eye: ({self.eye}), plane: ({self.plane})"


if __name__ == "__main__":
    c = Viewer3D(Point3D(0, 5, 5), Plane(Point3D(5, 0, 0), 10, 10))
    print(c.see(Point3D(10, -1, 0)))
    print(c.translatePoint(c.see(Point3D(10, -1, 0))))
    print(c.see(Point3D(10, -5, 0)))
    print(c.translatePoint(c.see(Point3D(10, -5, 0))))
