import constants as c
from canString import *

#Driver channel utilizes 500 000 bit/s speed
class Driver(can2A):
    
    def __init__(self, msgType):
        super().__init__(500000, False, False, msgType)
    
    
class DashboardAccumulatorData(Driver):

    def __init__(self):
        super().__init__(c.dashAccumulator)


class DashboardMotorData(Driver):

    def __init__(self):
        super().__init__(c.dashMotor)


class DashboardVehicleData(Driver):

    def __init__(self):
        super().__init__(c.dashVehicle)


class DriverWheelControls(Driver):

    def __init__(self):
        super().__init__(c.driverWheel)


class DriverDriverSettings(Driver):

    def __init__(self):
        super().__init__(c.driverSettings)


class DriverDrivingInputs(Driver):

    def __init__(self):
        super().__init__(c.driverInputs)

class DriverVehicleDynamics(Driver):

    def __init__(self):
        super().__init__(c.vehicleDynamics)

