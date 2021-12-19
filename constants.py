'''
This is a .py file to store and utilize specific constants for CAN message string
It is organized by channel with variable names based on given descriptions.
format: description[message id, data length]
taken from CAN_Traffic_Calculations.xlsx
'''

import channel_Driver
import channel_AMK
import channel_Cooling

# Driver channel
dashAccumulator = [0x190, 40]
dashMotor = [0x1F4, 32]
dashVehicle = [0xC8, 18]
driverWheel = [0X12C, 3]
driverSettings = [0X258, 16]
driverInputs = [0x64, 48]
vehicleDynamics = [0x2BC, 40]


dictDriver = {
    1: channel_Driver.DashboardAccumulatorData,
    2: channel_Driver.DashboardMotorData,
    3: channel_Driver.DashboardVehicleData,
    4: channel_Driver.DriverWheelControls,
    5: channel_Driver.DriverDriverSettings,
    6: channel_Driver.DriverDrivingInputs,
    7: channel_Driver.DriverVehicleDynamics
}

# Cooling channel
controlWords = [0x1000, 48]
statusWords = [0x1100, 40]
acknowledgement = [0x1200, 1]

dictCooling = {
    1: channel_Cooling.CoolingControlWords,
    2: channel_Cooling.CoolingStatusWords,
    3: channel_Cooling.CoolingAcknowledgement
}


# AMK channel
amkSetpoints1Inverter0 = [0x184, 64]
amkSetpoints1Inverter1 = [0x194, 64]
amkSetpoints1Inverter2 = [0x1A4, 64]
amkSetpoints1Inverter3 = [0x1B4, 64]

amkActualValues1Inverter0 = [0x283, 64]
amkActualValues2Inverter0 = [0x285, 64]
amkActualValues1Inverter1 = [0x293, 64]
amkActualValues2Inverter1 = [0x295, 64]
amkActualValues1Inverter2 = [0x2A3, 64]
amkActualValues2Inverter2 = [0x2A5, 64]
amkActualValues1Inverter3 = [0x2B3, 64]
amkActualValues2Inverter3 = [0x2B5, 64]


#BUG with dictAMK... apparently there is a circular import although I cannot find it
'''
dictAMK = {
    1: channel_AMK.AMKSetPoints1Inverter0,
    2: channel_AMK.AMKSetPoints1Inverter1,
    3: channel_AMK.AMKSetPoints1Inverter2,
    4: channel_AMK.AMKSetPoints1Inverter3,
    5: channel_AMK.AMKActualValues1Inverter0,
    6: channel_AMK.AMKActualValues2Inverter0,
    7: channel_AMK.AMKActualValues1Inverter1,
    8: channel_AMK.AMKActualValues2Inverter1,
    9: channel_AMK.AMKActualValues1Inverter2,
    10: channel_AMK.AMKActualValues2Inverter2,
    11: channel_AMK.AMKActualValues1Inverter3,
    12: channel_AMK.AMKActualValues2Inverter3
}
'''
