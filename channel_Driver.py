import constants as c
from canString import *


class Driver(can2A):
    
    def __init__(self, messageId, dataLength, data):
        super().__init__(messageId, 500000, False, False, data, dataLength)
    
    
class DashboardAccumulatorData(Driver):
    def __init__(self, data):
        ID = c.dashAccumulator[0]
        dataLen = c.dashAccumulator[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")

class DashboardMotorData(Driver):
    def __init__(self, data):
        ID = c.dashMotor[0]
        dataLen = c.dashMotor[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


class DashboardVehicleData(Driver):
    def __init__(self, data):
        ID = c.dashVehicle[0]
        dataLen = c.dashVehicle[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


class DriverWheelControls(Driver):
    def __init__(self, data):
        ID = c.driverWheel[0]
        dataLen = c.driverWheel[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message")


class DriverDriverSettings(Driver):
    def __init__(self, data):
        ID = c.driverSettings[0]
        dataLen = c.driverSettings[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


class DriverDrivingInputs(Driver):
    def __init__(self, data):
        ID = c.driverInputs[0]
        dataLen = c.driverInputs[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")

