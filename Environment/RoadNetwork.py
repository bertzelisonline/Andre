from Signals.I103_RoadNetwork import *

class RoadNetwork:
    def __init__(self,
                 timestamp_us: int,
                 road_segments: List[RoadNetwork],
                 lane_segments: List[LaneSegment],
                 list_of_routes: List[Route],
                 current_lane_index: int):
        self.current_lane_index = lane_segments[current_lane_index]
        # TODO: the road network consists not of a single road or lane, it consists of a set of road or lanes - please refactor the code
        self.road_category = road_segments
        self.lane_category = lane_category
        self.direction = direction
        self.id = id
        self.previousIndices = previousIndices
        self.nextIndices = nextIndices
        self.leftIndex = leftIndex
        self.rightIndex = rightIndex
        self.rightMarkingIndex = rightMarkingIndex
        self.leftMarkingIndex = leftMarkingIndex
