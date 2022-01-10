class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


class Point3D:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


class Plane:
    def __init__(self, p: Point3D, z_dimension: int, y_dimension: int) -> None:
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
    def __init__(self, direction: str, *args: object) -> None:
        super().__init__(*args)
        self.direction = direction

    def __str__(self) -> str:
        return f"Point didn't fit in {self.direction}-direction"

    def __repr__(self) -> str:
        return f"Point didn't fit in {self.direction}-direction"


class Viewer3D:

    def __init__(self, eye: Point3D, drawingplane: Plane):
        self.eye = eye
        self.plane = drawingplane
        self.eye_plane_distance = drawingplane.point.x - eye.x

    def see(self, p: Point3D) -> Point2D:
        my = (self.eye.y - p.y) / (self.eye.x - p.x)
        mz = (self.eye.z - p.z) / (self.eye.x - p.x)
        y = self.eye.y + my * self.eye_plane_distance
        if not (y >= self.plane.point.y and y < self.plane.point.y + self.plane.height):
            raise OutOfView("y")
        z = self.eye.z + mz * self.eye_plane_distance
        if not (z >= self.plane.point.z and z < self.plane.point.z + self.plane.width):
            raise OutOfView("z")
        return Point2D(z, y)

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
