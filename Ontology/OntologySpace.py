from owlready2 import *

# Imported by: https://cryptpad.fr/code/#/2/code/edit/J-n7EwtDLGwSWU0wvpX7e5la/

"""
TODO: Was wird hier gemacht? Inputs und Outputs beschreiben.
TODO: Denk an die self.
TODO: Im Constructor alle member variablen initialisieren
TODO: 
"""


class Ontology:
    def __init__(self, ontology_name: Name, ontology_path: Path, road_network: RoadNetwork):
        self.__ontology_name = ontology_name
        self.__ontology_path = ontology_path
        self.__road_network = road_network  # Current road network
        self.__ontology = None  # Initialize ontology

    # Printing name and path
    def print_ontolgy_name(self) -> None:
        print(self.__ontology_name)

    def print_ontology_path(self) -> None:
        print(self.__ontology_path)

    # Utilities
    def load_ontology(self) -> None:
        self.__ontology = get_ontology("file://" + self.__ontology + ".owl").load()

    def save_ontology(self) -> None:
        self.__ontology.save()

    # Getter for Ontology
    def get_ego_lane(self) -> lane_segment:
        return __road_network.current_lane

    # Setter for Ontology
    def set_ego_lane(self) -> None:
        self.__ontology.current_lane = get_ego_lane()

    # Ontology specific methods
    def add_lane_segment(individual: lane_segment) -> None:
        individual = ontology.lane_segment(individual)

    def add_road_category(individual: lane_segment) -> None:
        individual = ontology.road_category(individual)

    def add_vehicle(individual: lane_segment) -> None:
        individual = onto.vehicle(individual)

    # Ontology queries
    def is_right_lane_change_possible(lane: lane_segment) -> bool:
        if str(lane.left_of) != "[]" and str(lane.has_right_marking) == "[" + ontology_name + ".broken_line]":

            # Beispiel neu:
            # __ontology.right_lane = road_network.lanes.lane.left_of
            # __ontology.right_lane = road_network.lanes.right_lane[0]
            # __ontology.right_lane = road_network.lanes.str()

            right_lane = lane.left_of
            right_lane = right_lane[0]
            right_lane = str(right_lane)
            right_lane = right_lane.split(".")
            right_lane_ind = ontology.search(iri="*" + right_lane[1])[0]

            if str(right_lane_ind.is_occupied_by) == "[]" and str(
                    right_lane_ind.has_a_direction) == "[" + ontology + ".same_direction]" and str(
                right_lane_ind.has_a_category) != "[" + ontology + ".entry]":
                print("Lane Change to the right is possible")
                return True
            else:
                return False

    def is_left_lane_change_possible(lane: lane_segment) -> bool:
        if str(lane.right_of) != "[]" and str(lane.has_left_marking) == "[" + ontology_name + ".broken_line]":
            left_lane = lane.right_of
            left_lane = left_lane[0]
            left_lane = str(left_lane)
            left_lane = left_lane.split(".")
            left_lane_ind = ontology.search(iri="*" + left_lane[1])[0]

            if str(left_lane_ind.is_occupied_by) == "[]"
                and str(left_lane_ind.has_a_direction)
                == "[" + ontology_name + ".same_direction]"
                and str(left_lane_ind.has_a_category)
                != "[" + ontology_name + ".entry]":
                print("Lane Change to the left is possible")
                return True
            else:
                return False

    def is_lane_segment_in_front_existing(lane: lane_segment) -> bool:
        if str(lane.behind) != "[]":
            front_lane = lane.behind
            front_lane = front_lane[0]
            front_lane = str(front_lane)
            front_lane = front_lane.split(".")
            front_lane_ind = ontology.search(iri="*" + front_lane[1])[0]

            if str(front_lane_ind.is_occupied_by) == "[]":
                print("Lane Change to the front is possible")
                return True
            else:
                other_vehicle = front_lane_ind.is_occupied_by[0]
                other_vehicle = str(other_vehicle)
                other_vehicle = other_vehicle.split(".")
                other_vehicle_ind = ontology.search(iri="*" + other_vehicle[1])[0]

                if str(other_vehicle_ind.leaves) != "[]":
                    print("Lane Change to the front is possible")
                    return True
            # TODO: Add False Case

    def relation_left_of(left_lane: lane_segment, right_lane: lane_segment) -> None:
        if left_lane and right_lane:
            left_lane.left_of = [right_lane]
            print(str(left_lane) + " links von " + str(right_lane))
        else:
            print("individual " + str(left_lane) + " or " + str(right_lane) + " wasn't found")

    def relation_right_of(right_lane: lane_segment, left_lane: lane_segment) -> None:
        if right_lane and left_lane:
            right_lane.right_of = [left_lane]
            print(str(right_lane) + " rechts von " + str(left_lane))
        else:
            print("individual " + str(left_lane) + " or " + str(right_lane) + " wasn't found")

    def relation_in_front(front_lane: lane_segment, back_lane: lane_segment) -> None:
        if front_lane and back_lane:
            front_lane.in_front = [back_lane]
            print(str(front_lane) + " vor " + str(back_lane))
        else:
            print("individual " + str(front_lane) + " or " + str(back_lane) + " wasn't found")

    def relation_behind(back_lane: lane_segment, front_lane: lane_segment) -> None:
        if back_lane and front_lane:
            back_lane.behind = [front_lane]
            print(str(back_lane) + " hinter " + str(front_lane))
        else:
            print("individual " + str(back_lane) + " or " + str(front_lane) + " wasn't found")

    def relation_left_marking(lane: lane_segment, marking: lane_line) -> None:
        if lane and marking:
            lane.has_left_marking = [marking]

    def relation_right_marking(lane: lane_segment, marking: lane_line) -> None:
        if lane and marking:
            lane.has_right_marking = [marking]

    # Relation specific methods
    def relation_has_a_category(lane: lane_segment, marking: lane_line) -> None:
        if lane and category:
            lane.has_a_category = [category]

    def relation_has_a_direction(lane: lane_segment, road_direction: direction):
        if lane and road_direction:
            lane.has_a_direction = [road_direction]

    def relation_drives_on(vehicle: vehicle, lane: lane_segment):
        if vehicle and lane:
            vehicle.drives_on = [lane]

    def relation_leaves(first_vehicle: vehicle, second_vehicle: vehicle):
        if vehicle_1 and vehicle_2:
            vehicle_1.leaves = [vehicle_2]

    def relation_approach(first_vehicle: vehicle, second_vehicle: vehicle):
        if vehicle_1 and vehicle_2:
            vehicle_1.approach = [vehicle_2]

    # Ontology runner
    def create_ontology_space(self) -> None:
        # add individuals and relations:
        # create individuals:
        # lane lines
        broken_line = ontology.lane_line("broken_line")
        continuous_line = ontology.lane_line("continuous_line")

        # directions
        same_direction = ontology.direction("same_direction")
        opposite_direction = ontology.direction("opposite_direction")

        # road categories
        add_road_category("highway")
        add_road_category("entry")
        add_road_category("exit")

        # lane segments
        add_lane_segment("lane_1")
        add_lane_segment("lane_3")
        add_lane_segment("lane_4")
        add_lane_segment("lane_2")

        # vehicles
        add_vehicle("ego_vehicle")
        add_vehicle("car_2")

        # add relations:
        # left of / right of
        relation_left_of(ontology.lane_1, ontology.lane_2)
        relation_right_of(ontology.lane_2, ontology.lane_1)

        # in front/behind
        relation_in_front(ontology.lane_3, ontology.lane_1)
        relation_in_front(ontology.lane_4, ontology.lane_2)

        # lane_line
        relation_left_marking(ontology.lane_1, continuous_line)
        relation_left_marking(ontology.lane_2, broken_line)
        relation_right_marking(ontology.lane_1, broken_line)
        relation_right_marking(ontology.lane_2, continuous_line)

        # category
        relation_has_a_category(ontology.lane_1, ontology.highway)

        # direction
        relation_has_a_direction(ontology.lane_1, same_direction)
        relation_has_a_direction(ontology.lane_2, same_direction)

        # vehicle occupies
        relation_drives_on(ontology.car_2, ontology.lane_3)

        # approach / leave
        relation_leaves(ontology.ego_vehicle, ontology.car_2)

        # Reasoner
        # sync_reasoner()
        # query
        # check right lane change
        right_lane_change(ontology.lane_1)
        left_lane_change(ontology.lane_2)
        front_lane_change(ontology.lane_1)