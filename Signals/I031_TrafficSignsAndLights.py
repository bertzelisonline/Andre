from enum import Enum
from typing import List

from Signals.AbstractSignals import AbstractSignal
from Signals.I084_Points import Point3D


class MainSignClass(Enum):
    UNKNOWN = 0
    END_OF_SPEED_LIMIT = 1
    END_OF_NO_OVERTAKING = 2
    STOP_LINE = 3

    SPEED_LIMIT10 = 4
    SPEED_LIMIT20 = 5
    SPEED_LIMIT30 = 6
    SPEED_LIMIT40 = 7
    SPEED_LIMIT50 = 8
    SPEED_LIMIT60 = 9
    SPEED_LIMIT70 = 10
    SPEED_LIMIT80 = 11
    SPEED_LIMIT90 = 12
    SPEED_LIMIT100 = 13
    SPEED_LIMIT110 = 14
    SPEED_LIMIT120 = 15
    SPEED_LIMIT130 = 16
    SPEED_LIMIT140 = 17
    SPEED_LIMIT150 = 18

    STOP_AHEAD = 19
    YIELD = 20
    GIVE_WAY_AHEAD = 21
    TRAFFIC_LIGHT = 22
    TRAFFIC_SIGNALS_AHEAD = 23
    ROUNDABOUT_AHEAD = 24
    TWO_WAY_TRAFFIC_AHEAD = 25
    UNCONTROLLED_RAILROAD_CROSSING_AHEAD = 26
    LEVEL_RAILROAD_CROSSING_WITH_BARRIERS_AHEAD = 27
    TRAM_OR_STREETCAR_CROSSING = 28
    RAILROAD_CROSSBUCK = 29
    LEVEL_CROSSING = 30
    CROSSROADS_AHEAD = 31
    JUNCTION_WITH_A_SIDE_ROAD_AHEAD = 32

    SCHOOL_ZONE = 33
    CHILDREN_PLAYGROUND_AHEAD = 34
    PEDESTRIAN_CROSSING_AHEAD = 35
    PEDESTRIANS_ON_ROAD_AHEAD = 36
    DOMESTIC_ANIMALS = 37
    WILD_ANIMALS = 38
    CYCLISTS_CROSSING = 39
    TRUCKS_CROSSING = 40
    EQUESTRIANS = 41

    ROADWORKS = 42
    OTHER_DANGER = 43

    STOP = 44
    YIELD_GIVE_WAY = 45
    YIELD_TO_ONCOMING_TRAFFIC = 46
    PRIORITY_ROAD = 47

    NO_ENTRY = 48
    ROAD_CLOSED = 49
    VEHICLES_PROHIBITED = 50
    NO_MOTOR_VEHICLES = 51
    NO_LEFT_TURN = 52
    NO_RIGHT_TURN = 53
    NO_U_TURN = 54
    NO_OVERTAKING = 55
    NO_PARKING = 56
    NO_STOPPING = 57

    PROCEED_STRAIGHT_NO_TURNS = 58
    TURN_RIGHT = 59
    TURN_RIGHT_AHEAD = 60
    PROCEED_STRAIGHT_OR_TURN_RIGHT = 61
    KEEP_RIGHT = 62
    KEEP_LEFT = 63
    PASS_ON = 64
    PASS_ON_EITHER_SIDE = 65
    ROUNDABOUT = 66
    OVERTAKING_PERMITTED = 67
    PEDESTRIANS_ONLY = 68
    BICYCLES_ONLY = 69
    SHARED_USE_PATH = 70
    PUBLIC_TRANSIT = 71

    ONE_WAY_STREET = 72
    TWO_WAY_TRAFFIC = 73
    PEDESTRIAN_CROSSING = 74
    BUMP_IN_ROAD = 75
    DEAD_END = 76
    ESCAPE_LANE = 77
    TUNNEL = 78
    SPEED_LIMIT_ZONE = 79
    NO_PARKING_ZONE = 80
    PARKING_ZONE = 81
    HOSPITAL = 82
    BUS_STOP = 83
    TRAIN_STATION = 84
    AIRPORT = 85
    CONTROLLED_ACCESS_HIGHWAY_BEGINS = 86
    FREEWAY_ENDS = 87
    CUSTOMS_POST = 88
    NATIONAL_HIGHWAY = 89

    NUMBER_OF_ENTRIES = 90


class Position:
    def __init__(self, relative_position: Point3D, arc_length: float):
        self.relative_position = relative_position
        self.arc_length = arc_length


class SignalTrafficSign(AbstractSignal):
    def __init__(self,
                 identification: int,
                 main_sign_classification: MainSignClass,
                 supplemental_sign: List[MainSignClass],
                 temporary: bool,
                 operation_hours: str,
                 position: Position):
        self.id = identification
        self.main_sign_classification = main_sign_classification
        self.supplemental_sign = supplemental_sign
        self.temporary = temporary
        self.operation_hours = operation_hours
        self.position = position

class SignalTrafficLight(AbstractSignal):
    def __init__(self,
                 additional_sign: MainSignClass,
                 temporary: bool,
                 operation_hours: str,
                 signal_group_id: int,
                 position: Position):
        self.additional_sign = additional_sign
        self.temporary = temporary
        self.operation_hours = operation_hours
        self.signal_group_id = signal_group_id
        self.position = position
