from enum import Enum

from Signals.AbstractSignals import AbstractSignal


class SensorMinorType(Enum):
    UNKNOWN = 0
    RADAR_MRR = 1
    RADAR_SWA = 2
    RADAR_FTEN = 3
    RADAR_COCOON = 4
    RADAR_ARS408 = 5
    LIDAR_SCALA = 6
    LIDAR_VLP16 = 7
    LIDAR_VLP32 = 8
    LIDAR_VLP64 = 9
    LIDAR_HS40 = 10
    LIDAR_HS40P = 11
    LIDAR_HS64 = 12
    CAMERA_ME = 13
    ACC_REAL_TARGET = 14
    ACC_PASSING_PREVENTION_TARGET = 15
    ACC_BOOST_TARGET = 16
    IMU_XSENS = 17
    IMU_ADMA = 18
    V2X = 19
    FUSION_OBJECT = 20
    FUSION_LANE = 21
    FUSION_FREESPACE = 22
    FUSION_GRID = 23
    NUMBER_OF_ENTRIES = 24


class SensorMajorType(Enum):
    UNKNOWN = 0
    LIDAR = 1
    RADAR = 2
    CAMERA = 3
    IMU = 4
    V2X = 5
    FUSION = 6
    ACC = 7
    ENVIRONMENT = 8
    ADPL_MODULE = 9
    NUMBER_OF_ENTRIES = 10


class SignalSensorSource(AbstractSignal):
    def __init__(self, sensor_minor_type: SensorMinorType, sensor_major_type: SensorMajorType):
        self.sensor_minor_type = sensor_minor_type
        self.sensor_major_type = sensor_major_type
