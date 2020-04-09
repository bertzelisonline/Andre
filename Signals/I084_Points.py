from Signals.AbstractSignals import AbstractSignal

class SphericalPoints(AbstractSignal):
    def __init__(self, latitude: float, longitude: float, height: float):
        self.latitude = latitude
        self.longitude = longitude
        self.height = height


class Point3D(AbstractSignal):
    def __init__(self, x_coordinate: float, y_coordinate: float, z_coordinate: float):
        self.x_cooridnate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate
