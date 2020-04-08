from enum import Enum

from Signals.AbstractSignal import AbstractSignal
from Signals.SignalACCPTObject import SignalACCPTObjectObjectClass


class RoadCategory(Enum):
    UNKNOW = 0 #road is an unknwon road
    OFF_ROAD = 1 # off road (sand, gravel etc.)
    LOCAL_ROAD = 2 # road is a small local road (villages etc.)
    PROVINCE_ROAD = 3 # road is small province road (owned and maintained by countries province)
    COUNTRY_ROAD = 4 # road is a bigger country road (owned and maintained by country/county)
    EXPRESSWAY = 5 # road is not a highway but designed for faster traveling than country road
    HIGHWAY = 6 # road is highway
    INTERSTATE_ROAD	= 7 # road is a big interstate road / motorway / Autobahn connecting counties within a state
    ROUNDABOUT = 8 # round about
    #DIE 9 FEHLT!!!!!!!!!!!!!!! TODO: Add the 9th value!
    BUSSTOP	= 10 #
    SIDEWALK = 11 #
    PEDESTRIAN_CROSSING	= 12 # 
    RAIL_ROAD_CROSSING = 13 #
    GRASSSTRIP = 14 #
    TOLLGATE = 15 #
    EMERGENCY_BAY = 16 #
    

class SurfaceMaterial(Enum):
    UNKNOWN	= 0	# road surface is unknown
    ASPHALT = 1				# hard
    ROUGH = 2					# cobble stone
    DIRT = 3					# loose
    NUMBER_OF_ENTRIES = 4 # NoE


class LaneCategory(Enum):
    UNKNOWN = 0 # Lane category is unknown
    NORMAL = 1 # TBD: What does this mean?
    ENTRY = 2 # road is an entry to a higher road category (highway etc.)
    EXIT = 3 # road is an exit to a lower road category (e.g. from highway to Interstate)
    BUSLANE = 4 #
    MERGING_LEFT = 5 # lane will be merged with left lane
    MERGING_RIGHT = 6 # lane will be merged with right lane
    TERMINATING	= 7 # lane will terminate abruptly. Lane change necessary most likely.
    SLOW = 8 # lane for slow moving vehicles
    SPECIAL	= 9 # lane for special vehicles (e.g. busses, taxis)
    EMERGENCY = 10 # emergency lane, shoulder
    PARKING	= 11 #
    TEMPORARY = 12 #
    PAVEMENT = 13 #
    # BIKE = designated bike lane TODO: WAAAAAAAAAAAAAAAAAAAAAAAAAAS?
    NUMBER_OF_ENTRIES = 14 # Total number of lane category entries

class ParkingType(Enum):
    UNKNOWN = 0
    NO_STOPPING = 1 # Absolute no stopping and no parking restriction.
    NO_PARKING_STOPPING_YES = 2	# Parking is forbidden, but to stop is allowed.
    PARKING_ALLOWED = 3 # Parking and stopping is allowed
    PARKING_ALLOWED_HALF_PAVEMENT =	4 # Parking is allowed if half of the vehicle is parking on the pavement.
    PARKING_ALLOWED_FULL_PAVEMENT =	5 # Parking is allowed on the pavement. Only available for ELaneCategory::PAVEMENT.
    NUMBER_OF_ENTRIES = 6


class RightOfWay(Enum):
    UNKNOWN = 0
    RIGHT_OF_WAY = 1
    NO_RIGHT_OF_WAY = 2
    NOT_EXPLICIT_DEFINED = 3


class Direction(Enum):
    NOT_DEFINED = 0
    SAME = 1 # Object points in the same direction as this object
    CONTRA = 2 # Object points in the contra / opposite direction as this object
    BOTH = 3 # in both directions possible. This is not an option to describe relation between lane and lane marking.
    NUMBER_OF_ENTRIES = 4 # NoE

class LaneSegmentPointLine(Enum):
    id = 0
    roadSegmentIndex = roadSegmentIndex #2^64 -1 = lane segment does not belong to any road.
    indexRoutes = indexRoutes

    previousIndices = previousIndices # Indices of lanes which flow into / open out into this lane segment.
    nextIndices = nextIndices # Indices of lane segments which origin is within this lane segment.
    crossingIndices = crossingIndices # Indices of lane which do cross this lane. Without having a possible transition from to each other.
    leftIndex = leftIndex # 2^64 -1 = no neighbor. Index of lane segment to the left of this
    leftDrivingDirection = leftDrivingDirection # Is neighbour lane in same direction as this lane or is it the contra flow direction?
    rightIndex = rightIndex # 2^64 -1 = no neighbor. Index of lane segment to the right of this
    rightDrivingDirection = rightDrivingDirection # Is neighbour lane in same direction as this lane or is it the contra flow direction?
    speedLimit = speedLimit # 0 means not defined.
    speedMinimum = speedMinimum # 0 means not defined.
    speedRecommended = speedRecommended # 0 means not defined.
    rightMarkingIndex = rightMarkingIndex
    rightMarkingDirection = rightMarkingDirection # Is the right lane marking in the same direction as this lane or is the lane marking in direction of contra flow lanes? Note neighbor lanes CAN share a lane marking and if the neighbor lane is a contra flow lane, the lane marking might point in a different direction compared to one of the lane centers. Direction is also defined by the lane points, which start somewhere and continue in a certain direction.
    leftMarkingIndex = leftMarkingIndex
    leftMarkingDirection = leftMarkingDirection # Is the left lane marking in the same direction as this lane or is the lane marking in direction of contra flow lanes? Note neighbor lanes CAN share a lane marking and if the neighbor lane is a contra flow lane, the lane marking might point in a different direction compared to one of the lane centers. Direction is also defined by the lane points, which start somewhere and continue in a certain direction.
    remainingLength = remainingLength # Minimum of the total segment length and arc length from actual position to the end of this lane segment.
    drivingLine = drivingLine # optimum driving line / path. Keep in mind to decenter the vehicle in the lane based on map information (f.ex. a pothole).
    
    intersectionID = intersectionID # 0 = This lane is not part of an intersection
    laneCategory = laneCategory
    directionRegardingRoute = directionRegardingRoute # is this lane in direction of primary route?
	trafficLights = trafficLights
	surface = surface
    parkingType = parkingType
    roadCategory = roadCategory
    rightOfWay= rightOfWay # regarding the lanes which do enter crossings.
    driveable = driveable

class OptimizationCriterion(Enum):
    UNKNOWN = UNKNOWN # 00 - 
	DISTANCE = DISTANCE
	TIME = TIME
	NUMBER_OF_ENTRIES = NUMBER_OF_ENTRIES # 02 - 

class RouteElement(Enum):
    typeRoad = typeRoad # if true index defines a road element, which is part of the route. If false, index defines a lane segment as part of the route.
    roadSegmentIndex = roadSegmentIndex
    lanesIndices = lanesIndices

class Route(Enum):
    elements = elements # This array needs to be sort from route start in direction to route end.
	optimizationCriterion = optimizationCriterion
	type = type # -1 = not part of any route. 0 = part of route. 1 = part of alternative route 1. 2 = part of alternative route 2. ...
# TODO: type is not valid name!!!

class RoadSegment(Enum):
    id = id
    #TODO: ID seems to be not valid
    lanesIndices = lanesIndices
    indexRoutes = indexRoutes
    bordersIndices = bordersIndices


    speedLimit = speedLimit # 255 means speed limit is defined by lanes. 0 means not defined.
    speedMinimum = speedMinimum # 255 means speed limit is defined by lanes. 0 means not defined.
    speedRecommended = speedRecommended # 255 means speed limit is defined by lanes. 0 means not defined.

    remainingLength = remainingLength # Minimum of the total segment length and arc length from actual position to the end of this road segment.
    name = name
    roadCategory = roadCategory
    rightOfWay = rightOfWay # regarding the lanes which do enter crossings.
    oneWay = oneWay
    tunnel = tunnel
    adVerified = adVerified # Lane segment as well as map data of this segment are verified for autonomous driving.

    country[2] = country[2] # ISO 3166-1 ALPHA-2 Release 2007-03 country code of current position; 0 stands for unknown. Valid values are those specified by ISO 3166-1 numeric [15].
    trafficRightHand = trafficRightHand # false stands for Driving Side Left. True stands for Driving Side Right. Default is 1.

class RoadNetworkPointLine(Enum):
    timestamp_us = timestamp_us # timestamp [us]
	sensorSource = sensorSource # module source
	
	roadSegments = roadSegments
	laneSegments = laneSegments
    laneMarking = laneMarking
	routes = routes # possible routes to drive
	currentLaneIndex = currentLaneIndex # Index of the lane ego vehicle is currently driving on
	
	metricUnit = metricUnit # Defines speed limit units. False stands for miles per hour (mph). True stands for kilometers/hour (km/h). Default is 1.
	
	routeArguments = routeArguments # start and end of route
	fetchArguments = fetchArguments # map corridor arguments. What corridor was requested from fetcher?
