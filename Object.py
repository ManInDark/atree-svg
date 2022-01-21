from abc import ABCMeta, abstractmethod
from Viewer3D import Point3D


class OutOfPoints(Exception):
    pass


class Object(metaclass=ABCMeta):

    """
    Base class for all other object.
    """

    def __init__(self, starting_point: Point3D, points: int) -> None:
        self.starting_point = starting_point
        self.points = points

    @abstractmethod
    def nextPoint(self) -> Point3D:
        pass
