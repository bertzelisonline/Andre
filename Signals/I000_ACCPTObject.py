from enum import Enum

from Signals.AbstractSignal import AbstractSignal


class SignalACCPTObjectObjectClass(Enum):
    UNKNOWN = 0  # The object class of the object is unknown
    CAR = 1  # This object is a car
    TRUCK = 2  # This object is a truck


class SignalACCPTObject(AbstractSignal):
    """
    This signal-class is similar to the 'SensObjList', but it's length is '1', because it contains information
    about the ACCPrimary-Target. The master-signal consists of the following signals:
    long - Identification number of the selected object
    float ObjectConfidence - This is the confidence that the object exists, in SUMO it's always '1.0'
    float ObjectProbability - Probability that the object is in the host-path
    unsigned long ObjectAge - This is the age of the object, counting in timesteps
    long long Timestamp
    float ObjectLaneAssignment - Object-assignment to the lane: 1 or -1 in the left or right lane, 0 is in host-lane
    float ObjectTimeToCollision - Time to collision with the object: 0 collision is not possible
    ENUM ObjectClass - Object class of the object, in SUMO the objects are always 'CAR'
    float ObjectClassConfidence - Confidence, that the object belongs to the defined object-class
    float ObjectPosX - X-Position of the object
    float ObjectPosXStdDev - Standard deviation of the X-Position of the object, in SUMO it's always '0.0'
    float ObjectPosY - Y-Position of the object
    float ObjectPosYStdDev - Standard deviation of the Y-Position of the object, in SUMO it's always '0.0'
    float ObjectPosZ - Z-Position of the object, in SUMO it's always '0.0'
    float ObjectPosZStdDev - Standard deviation of the Z-Position of the object, in SUMO it's always '0.0'
    float ObjectCourseAngle - Object orientation from the host-path as zero-angle
    float ObjectCourseAngleStdDev - Standard deviation of the object orientation, in SUMO it's always '0.0'
    float ObjectRelSpeedX - Relative speed of the object in X-direction
    float ObjectRelSpeedXStdDev - Standard deviation of the object in X-direction, in SUMO it's always '0.0'
    float ObjectRelSpeedY - Relative speed of the object in Y-direction
    float ObjectRelSpeedYStdDev - Standard deviation of the object in Y-direction, in SUMO it's always '0.0'
    float ObjectRelSpeedZ - Relative speed of the object in Z-direction
    float ObjectRelSpeedZStdDev - Standard deviation of the object in Z-direction, in SUMO it's always '0.0'
    float ObjectAbsSpeedX - Absolute speed of the object in X-direction
    float ObjectAbsSpeedXStdDev - Standard deviation of the object in X-direction, in SUMO it's always '0.0'
    float ObjectAbsSpeedY - Absolute speed of the object in Y-direction
    float ObjectAbsSpeedYStdDev - Standard deviation of the object in Y-direction, in SUMO it's always '0.0'
    float ObjectAbsSpeedZ - Absolute speed of the object in Z-direction
    float ObjectAbsSpeedZStdDev - Standard deviation of the object in Z-direction, in SUMO it's always '0.0'
    float ObjectRelAccX - Acceleration of the object in X-direction
    float ObjectRelAccXStdDev - Standard deviation of the object in X-direction, in SUMO it's always '0.0'
    float ObjectRelAccY - Acceleration of the object in Y-direction
    float ObjectRelAccYStdDev - Standard deviation of the object in Y-direction, in SUMO it's always '0.0'
    float ObjectRelAccZ - Acceleration of the object in Z-direction
    float ObjectRelAccZStdDev - Standard deviation of the object in Z-direction, in SUMO it's always '0.0'
    float ObjectWidth
    float ObjectWidthStdDev - Standard deviation of the objects width, in SUMO it's always '0.0'
    float ObjectLength
    float ObjectLenghtStdDev - Standard deviation of the objects length, in SUMO it's always '0.0'
    """

    def __init__(self,

                 var_long_object_id: int,
                 var_float_object_confidence: float,
                 var_float_object_probability: float,
                 var_ulong_object_age: int,
                 var_longlong_timestamp: int,
                 var_float_object_lane_assignment: int,
                 var_float_object_time_to_collision: float,
                 var_enum_object_class: SignalACCPTObjectObjectClass,
                 var_float_object_class_confidence: float,
                 var_float_object_pos_x: float,
                 var_float_object_pos_x_std_dev: float,
                 var_float_object_pos_y: float,
                 var_float_object_pos_y_std_dev: float,
                 var_float_object_pos_z: float,
                 var_float_object_pos_z_std_dev: float,
                 var_float_object_course_angle: float,
                 var_float_object_course_angle_std_dev: float,
                 var_float_object_rel_speed_x: float,
                 var_float_object_rel_speed_x_std_dev: float,
                 var_float_object_rel_speed_y: float,
                 var_float_object_rel_speed_y_std_dev: float,
                 var_float_object_rel_speed_z: float,
                 var_float_object_rel_speed_z_std_dev: float,
                 var_float_object_abs_speed_x: float,
                 var_float_object_abs_speed_x_std_dev: float,
                 var_float_object_abs_speed_y: float,
                 var_float_object_abs_speed_y_std_dev: float,
                 var_float_object_abs_speed_z: float,
                 var_float_object_abs_speed_z_std_dev: float,
                 var_float_object_rel_acc_x: float,
                 var_float_object_rel_acc_x_std_dev: float,
                 var_float_object_rel_acc_y: float,
                 var_float_object_rel_acc_y_std_dev: float,
                 var_float_object_rel_acc_z: float,
                 var_float_object_rel_acc_z_std_dev: float,
                 var_float_object_width: float,
                 var_float_object_width_std_dev: float,
                 var_float_object_length: float,
                 var_float_object_length_std_dev: float,
                 ):
        self.long_object_id = var_long_object_id
        self.float_object_confidence = var_float_object_confidence
        self.float_object_probability = var_float_object_probability
        self.ulong_object_age = var_ulong_object_age
        self.longlong_timestamp = var_longlong_timestamp
        self.float_object_lane_assignment = var_float_object_lane_assignment
        self.float_object_time_to_collision = var_float_object_time_to_collision
        self.enum_object_class = var_enum_object_class
        self.float_object_class_confidence = var_float_object_class_confidence
        self.float_object_pos_x = var_float_object_pos_x
        self.float_object_pos_x_std_dev = var_float_object_pos_x_std_dev
        self.float_object_pos_y = var_float_object_pos_y
        self.float_object_pos_y_std_dev = var_float_object_pos_y_std_dev
        self.float_object_pos_z = var_float_object_pos_z
        self.float_object_pos_z_std_dev = var_float_object_pos_z_std_dev
        self.float_object_course_angle = var_float_object_course_angle
        self.float_object_course_angle_std_dev = var_float_object_course_angle_std_dev
        self.float_object_rel_speed_x = var_float_object_rel_speed_x
        self.float_object_rel_speed_x_std_dev = var_float_object_rel_speed_x_std_dev
        self.float_object_rel_speed_y = var_float_object_rel_speed_y
        self.float_object_rel_speed_y_std_dev = var_float_object_rel_speed_y_std_dev
        self.float_object_rel_speed_z = var_float_object_rel_speed_z
        self.float_object_rel_speed_z_std_dev = var_float_object_rel_speed_z_std_dev
        self.float_object_abs_speed_x = var_float_object_abs_speed_x
        self.float_object_abs_speed_x_std_dev = var_float_object_abs_speed_x_std_dev
        self.float_object_abs_speed_y = var_float_object_abs_speed_y
        self.float_object_abs_speed_y_std_dev = var_float_object_abs_speed_y_std_dev
        self.float_object_abs_speed_z = var_float_object_abs_speed_z
        self.float_object_abs_speed_z_std_dev = var_float_object_abs_speed_z_std_dev
        self.float_object_rel_acc_x = var_float_object_rel_acc_x
        self.float_object_rel_acc_x_std_dev = var_float_object_rel_acc_x_std_dev
        self.float_object_rel_acc_y = var_float_object_rel_acc_y
        self.float_object_rel_acc_y_std_dev = var_float_object_rel_acc_y_std_dev
        self.float_object_rel_acc_z = var_float_object_rel_acc_z
        self.float_object_rel_acc_z_std_dev = var_float_object_rel_acc_z_std_dev
        self.float_object_width = var_float_object_width
        self.float_object_width_std_dev = var_float_object_width_std_dev
        self.float_object_length = var_float_object_length
        self.float_object_length_std_dev = var_float_object_length_std_dev

        # optional tag field
        self.tag = None

    @staticmethod
    def create_emtpy():
        # creates an instance of the ACCPT object where no field is set, except the "is empty" field.
        return SignalACCPTObject(
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None).set_empty(True)

    def get_car_id(self):
        return self.tag

    def to_string(self):  # String-representation inside the object
        return "objectId=" + str(self.long_object_id) + ", timestamp=" + str(self.longlong_timestamp)\
                + ", objectClass=" + str(self.enum_object_class) + ", tag=" + str(self.tag)
