from enum import Enum

from Signals.AbstractSignal import AbstractSignal


class ObjectMoveState(Enum):
    UNKNOWN = 0  # Move state is unknown
    PROBABLE_STATIC = 1  # Object is probably static
    STATIC_OBJ = 2  # Object is static
    PROBABLE_DYNAMIC = 3  # Object is probably dynamic
    DYNAMIC = 4  # Object is dynamic
    MOVABLE = 5  # Object is movable, when it moved, but now it doesn't move
    NUMBER_OF_ENTRIES = 6 # Number of entries


class ObjectClass(Enum):
    UNKNOWN = 0  #
    PEDESTRIAN = 1
    TWO_WHEEL = 2
    CAR = 3
    BUS = 4
    TRUCK = 5
    TRAM = 6
    OTHER = 7
    NUMBER_OF_ENTRIES = 8


class SignalSensObjList(AbstractSignal):
    """

    """

    def __init__(self,
                 identification: int,
                 timestamp_us: int,
                 position: SphericalPoints, #TODO: implement sphericalpoints
                 heading: float,
                 heading_standard_deviation: float,
                 reference_point: int,
                 move_state: ObjectMoveState,
                 object_class: ObjectClass,
                 velocity_x: float,
                 velocity_x_standard_deviation: float,
                 velocity_y: float,
                 velocity_y_standard_deviation: float,
                 length: float,
                 length_standard_deviation: float,
                 width: float,
                 width_standard_deviation: float,
                 height: float,
                 height_standard_deviation: float,
                 confidence_classification: float,
                 confidence_existence: float):
        self.id = identification
        self.timestamp_us = timestamp_us
        self.position = position
        self.heading = heading
        self.heading_standard_deviation = heading_standard_deviation
        self.reference_point = reference_point
        self.move_state = move_state
        self.object_class = object_class
        self.velocity_x = velocity_x
        self.velocity_x_standard_deviation = velocity_x_standard_deviation
        self.velocity_y = velocity_y
        self.velocity_y_standard_deviation = velocity_y_standard_deviation
        self.length = length
        self.length_standard_deviation = length_standard_deviation
        self.width = width
        self.width_standard_deviation = width_standard_deviation
        self.height = height
        self.height_standard_deviation = height_standard_deviation
        self.confidence_classification = confidence_classification
        self.confidence_existence = confidence_existence

    def to_string(self):  # String-representation inside the object
        return ""
