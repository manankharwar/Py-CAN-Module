'''
This is a .py file to store and utilize specific constants for CAN message string
It is organized by channel with variable names based on given descriptions.
format: description[message id, data length in bytes]
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


# Cooling channel
controlWords = [0x1000, 48]
statusWords = [0x1100, 40]
acknowledgement = [0x1200, 1]


# AMK channel

#amk channel constants for description: SetPoints_Inverter_
amkSP1I0 = [0x184, 64]
amkSP1I1 = [0x194, 64]
amkSP1I2 = [0x1A4, 64]
amkSP1I3 = [0x1B4, 64]

#amk channel constants for description: ActualValues_Inverter_
amkAV1I0 = [0x283, 64]
amkAV2I0 = [0x285, 64]
amkAV1I1 = [0x293, 64]
amkAV2I1 = [0x295, 64]
amkAV1I2 = [0x2A3, 64]
amkAV2I2 = [0x2A5, 64]
amkAV1I3 = [0x2B3, 64]
amkAV2I3 = [0x2B5, 64]

