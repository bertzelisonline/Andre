from Signals.I103_RoadNetwork import SignalsRoadNetwork

class RoadNetwork:
    def __init__(self, road_category, lane_category, direction, id, previousIndices, nextIndices, leftIndex, rightIndex,rightMarkingIndex, leftMarkingIndex):

        self.road_category = road_category
        self.lane_category = lane_category
        self.direction = direction
        self.id = id
        self.previousIndices = previousIndices
        self.nextIndices = nextIndices
        self.leftIndex = leftIndex
        self.rightIndex = rightIndex
        self.rightMarkingIndex = rightMarkingIndex
        self.leftMarkingIndex = leftMarkingIndex
