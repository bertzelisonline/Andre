from enum import Enum
from typing import List

from Signals.AbstractSignal import AbstractSignal
from Signals.I000_ACCPTObject import SignalACCPTObjectObjectClass
from Signals.I031_TrafficSignsAndLights import SignalTrafficSign, SignalTrafficLight
from Signals.I085_SensorSource import SignalSensorSource

"""
  Enums: RoadCategory, SurfaceMaterial, LaneCategory, ParkingType, RightOfWay, Direction, OptimizationCriterion
"""


class RoadCategory(Enum):
    UNKNOW = 0  # road is an unknwon road
    OFF_ROAD = 1  # off road (sand, gravel etc.)
    LOCAL_ROAD = 2  # road is a small local road (villages etc.)
    PROVINCE_ROAD = 3  # road is small province road (owned and maintained by countries province)
    COUNTRY_ROAD = 4  # road is a bigger country road (owned and maintained by country/county)
    EXPRESSWAY = 5  # road is not a highway but designed for faster traveling than country road
    HIGHWAY = 6  # road is highway
    INTERSTATE_ROAD = 7  # road is a big interstate road / motorway / Autobahn connecting counties within a state
    ROUNDABOUT = 8  # round about
    MISSING_VALUE = 9  # DIE 9 FEHLT!!!!!!!!!!!!!!! TODO: Add the 9th value!
    BUSSTOP = 10  #
    SIDEWALK = 11  #
    PEDESTRIAN_CROSSING = 12  #
    RAIL_ROAD_CROSSING = 13  #
    GRASSSTRIP = 14  #
    TOLLGATE = 15  #
    EMERGENCY_BAY = 16  #


class SurfaceMaterial(Enum):
    UNKNOWN = 0  # road surface is unknown
    ASPHALT = 1  # hard
    ROUGH = 2  # cobble stone
    DIRT = 3  # loose
    NUMBER_OF_ENTRIES = 4  # NoE


class LaneCategory(Enum):
    UNKNOWN = 0  # Lane category is unknown
    NORMAL = 1  # TBD: What does this mean?
    ENTRY = 2  # road is an entry to a higher road category (highway etc.)
    EXIT = 3  # road is an exit to a lower road category (e.g. from highway to Interstate)
    BUSLANE = 4  #
    MERGING_LEFT = 5  # lane will be merged with left lane
    MERGING_RIGHT = 6  # lane will be merged with right lane
    TERMINATING = 7  # lane will terminate abruptly. Lane change necessary most likely.
    SLOW = 8  # lane for slow moving vehicles
    SPECIAL = 9  # lane for special vehicles (e.g. busses, taxis)
    EMERGENCY = 10  # emergency lane, shoulder
    PARKING = 11  #
    TEMPORARY = 12  #
    PAVEMENT = 13  #
    # BIKE = designated bike lane TODO: WAAAAAAAAAAAAAAAAAAAAAAAAAAS?
    NUMBER_OF_ENTRIES = 14  # Total number of lane category entries


class ParkingType(Enum):
    UNKNOWN = 0
    NO_STOPPING = 1  # Absolute no stopping and no parking restriction.
    NO_PARKING_STOPPING_YES = 2  # Parking is forbidden, but to stop is allowed.
    PARKING_ALLOWED = 3  # Parking and stopping is allowed
    PARKING_ALLOWED_HALF_PAVEMENT = 4  # Parking is allowed if half of the vehicle is parking on the pavement.
    PARKING_ALLOWED_FULL_PAVEMENT = 5  # Parking is allowed on the pavement. Only available for ELaneCategory::PAVEMENT.
    NUMBER_OF_ENTRIES = 6


class RightOfWay(Enum):
    UNKNOWN = 0
    RIGHT_OF_WAY = 1
    NO_RIGHT_OF_WAY = 2
    NOT_EXPLICIT_DEFINED = 3


class Direction(Enum):
    NOT_DEFINED = 0
    SAME = 1  # Object points in the same direction as this object
    CONTRA = 2  # Object points in the contra / opposite direction as this object
    BOTH = 3  # in both directions possible. This is not an option to describe relation between lane and lane marking.
    NUMBER_OF_ENTRIES = 4  # NoE


class OptimizationCriterion(Enum):
    UNKNOWN = 0
    DISTANCE = 1
    TIME = 2
    NUMBER_OF_ENTRIES = 3


"""
Classes for the main struct: LaneMarking, LaneSegment, RouteElement, Route, RoadSegment
"""


class LaneMarking:
    def __init__(self):
        pass  # TODO: implement lane markings


class Shape:
    def __init__(self):
        pass


class TrafficSign:
    def __init__(self):
        pass


class TrafficLight:
    def __init__(self):
        pass


class LaneSegment:
    def __init__(self,
                 identifiaction: int, road_segment_index: int, index_routes: List[int],
                 previous_indices: List[int], next_indices: List[int], crossing_indices: List[int],
                 left_index: int, left_driving_direction: Direction,
                 right_index: int, right_driving_direction: Direction,
                 speed_limit: int, speed_minimum: int, speed_recommended: int,
                 right_marking_index: int, right_marking_direction: Direction,
                 left_marking_index: int, left_marking_direction: Direction,
                 remaining_length: float,
                 driving_line: Shape,  # TODO: implement shape class
                 intersection_id: int,
                 lane_category: LaneCategory,
                 direction_regarding_route: Direction,
                 traffic_signs: List[SignalTrafficSign], traffic_lights: List[SignalTrafficLight],
                 road_surface: SurfaceMaterial,
                 parking_type: ParkingType,
                 road_category: RoadCategory, right_of_way: RightOfWay, is_driveable: bool):
        self.id = identifiaction
        self.road_segment_index = road_segment_index
        self.index_routes = index_routes

        self.previous_indices = previous_indices  # Indices of lanes which flow into / open out into this lane segment.
        self.next_indices = next_indices  # Indices of lane segments which origin is within this lane segment.
        self.crossing_indices = crossing_indices  # Indices of lane which do cross this lane. Without having a possible
        # transition from to each other.

        self.left_index = left_index  # 2^64 -1 = no neighbor. Index of lane segment to the left of this
        self.left_driving_direction = left_driving_direction  # Is neighbour lane in same direction as this lane or is
        # it the contra flow direction?
        self.right_index = right_index  # 2^64 -1 = no neighbor. Index of lane segment to the right of this
        self.right_driving_direction = right_driving_direction  # Is neighbour lane in same direction as this lane or
        # is it the contra flow direction?
        self.speed_limit = speed_limit  # 0 means not defined.
        self.speed_minimum = speed_minimum  # 0 means not defined.
        self.speed_recommended = speed_recommended  # 0 means not defined.
        self.right_marking_index = right_marking_index
        self.right_marking_direction = right_marking_direction  # Is the right lane marking in the same direction as
        # this lane or is the lane marking in direction of contra flow lanes? Note neighbor lanes CAN share a lane
        # marking and if the neighbor lane is a contra flow lane, the lane marking might point in a different direction
        # compared to one of the lane centers. Direction is also defined by the lane points,
        # which start somewhere and continue in a certain direction.
        self.left_marking_index = left_marking_index
        self.left_marking_direction = left_marking_direction  # Is the left lane marking in the same direction as this
        # lane or is the lane marking in direction of contra flow lanes? Note neighbor lanes CAN share a lane marking
        # and if the neighbor lane is a contra flow lane, the lane marking might point in a different direction
        # compared to one of the lane centers. Direction is also defined by the lane points, which start
        # somewhere and continue in a certain direction.
        self.remaining_length = remaining_length  # Minimum of the total segment length and arc length from actual
        # position to the end of this lane segment.
        self.driving_line = driving_line  # optimum driving line / path. Keep in mind to decenter the vehicle in the
        # lane based on map information (f.ex. a pothole).
        self.intersection_id = intersection_id  # 0 = This lane is not part of an intersection
        self.lane_category = lane_category
        self.direction_regarding_route = direction_regarding_route  # is this lane in direction of primary route?
        self.traffic_signs = traffic_signs
        self.traffic_lights = traffic_lights
        self.road_surface = road_surface
        self.parking_type = parking_type
        self.road_category = road_category
        self.right_of_way = right_of_way  # regarding the lanes which do enter crossings.
        self.is_driveable = is_driveable


class RouteElement:
    def __init__(self, type_of_road: bool, road_segment_index: int, lanes_indices: List[int]):
        self.type_of_road = type_of_road  # if true index defines a road element, which is part of the route.
        # If false, index defines a lane segment as part of the route.
        self.road_segment_index = road_segment_index
        self.lanesIndices = lanes_indices


class Route:
    def __init__(self, elements: List[RouteElement], optimization_criterion: List[OptimizationCriterion], type: int):
        self.elements = elements  # This array needs to be sort from route start in direction to route end.
        self.optimization_criterion = optimization_criterion
        self.type = type  # -1 = not part of any route. 0 = part of route. 1 = part of alternative route 1. 2 = part
        # of alternative route 2. ...


class RoadSegment:
    def __init__(self,
                 identification: int,
                 lanes_indices: List[int],
                 index_routes: List[int],
                 borders_indices: List[int],
                 speed_limit: int,
                 speed_minimum: int,
                 speed_recommended: int,
                 remaining_length: float,
                 name: str,
                 road_category: RoadCategory,
                 right_of_way: RightOfWay,
                 one_way: bool,
                 tunnel: bool,
                 ad_verified: bool,
                 country: List[int],
                 traffic_right_hand: bool):
        self.id = identification
        self.lanes_indices = lanes_indices
        self.index_routes = index_routes
        self.borders_indices = borders_indices

        self.speed_limit = speed_limit  # 255 means speed limit is defined by lanes. 0 means not defined.
        self.speed_minimum = speed_minimum  # 255 means speed limit is defined by lanes. 0 means not defined.
        self.speed_recommended = speed_recommended  # 255 means speed limit is defined by lanes. 0 means not defined.

        self.remaining_length = remaining_length  # Minimum of the total segment length and arc length from actual
        # position to the end of this road segment.
        self.name = name
        self.road_category = road_category
        self.right_of_way = right_of_way  # regarding the lanes which do enter crossings.
        self.one_way = one_way
        self.tunnel = tunnel
        self.ad_verified = ad_verified  # Lane segment as well as map data of this segment are verified for
        # autonomous driving.
        self.country = country  # ISO 3166-1 ALPHA-2 Release 2007-03 country code of current position; 0 stands for
        # unknown. Valid values are those specified by ISO 3166-1 numeric [15].
        self.traffic_right_hand = traffic_right_hand  # false stands for Driving Side Left. True stands for Driving
        # Side Right. Default is 1.


"""
This is the main struct of the interface
"""


class SignalRoadNetwork(AbstractSignal):
    def __init__(self,
                 timestamp_us: int,
                 sensor_source: SignalSensorSource,
                 road_segments: List[RoadSegment],
                 lane_segments: List[LaneSegment],
                 lane_markings: List[LaneMarking],
                 list_of_routes: List[Route],
                 current_lane_index: int,
                 metric_unit: bool,
                 route_arguments: SetRoute,  # TODO: implement setroute
                 fetch_arguments: FetchHorizon):  # TODO: implement fetchhorizon

        self.timestamp_us = timestamp_us  # timestamp [us]
        self.sensor_source = sensor_source  # module source

        self.road_segments = road_segments
        self.lane_segments = lane_segments
        self.lane_markings = lane_markings
        self.list_of_routes = list_of_routes  # possible routes to drive
        self.current_lane_index = current_lane_index  # Index of the lane ego vehicle is currently driving on

        self.metric_unit = metric_unit  # Defines speed limit units. False stands for miles per hour (mph). True stands
        # for kilometers/hour (km/h). Default is 1.

        self.route_arguments = route_arguments  # start and end of route
        self.fetch_arguments = fetch_arguments  # map corridor arguments. What corridor was requested from fetcher?

    def to_string(self):  # String-representation inside the object
        return ""
