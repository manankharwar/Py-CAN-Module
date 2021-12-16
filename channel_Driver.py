import constants as c
from canString import can2A


class Driver(can2A):
    
    def __init__(self, messageId, dataLength):
        super().__init__(messageId, 500000, False, True, None, dataLength)
    
    
class DashboardAccumulatorData(Driver):
    def __init__(self):
        ID = c.dashAccumulator_Id[0]
        dataLen = c.dashAccumulator_Id[1]
        super().__init__(ID, dataLen)


class DashboardMotorData(Driver):
    def __init__(self):
        ID = c.dashMotor[0]
        dataLen = c.dashMotor[1]
        super().__init__(ID, dataLen)


class DashboardVehicleData(Driver):
    def __init__(self):
        ID = c.dashVehicle[0]
        dataLen = c.dashVehicle[1]
        super().__init__(ID, dataLen)


class DriverWheelControls(Driver):
    def __init__(self):
        ID = c.driverWheel[0]
        dataLen = c.driverWheel[1]
        super().__init__(ID, dataLen)


class DriverDriverSettings(Driver):
    def __init__(self):
        ID = c.driverSettings[0]
        dataLen = c.driverSettings[1]
        super().__init__(ID, dataLen)


class DriverDrivingInputs(Driver):
    def __init__(self):
        ID = c.driverInputs[0]
        dataLen = c.driverInputs[1]
        super().__init__(ID, dataLen)

