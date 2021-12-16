'''
This is a .py file to store and utilize specific constants for CAN message string
It is organized by channel with variable names based on given descriptions.
format: description[message id, data length]
taken from CAN_Traffic_Calculations.xlsx
'''

# Driver channel
dashAccumulator= [0x190, 40]
dashMotor = [0x1F4, 32]
dashVehicle = [0xC8, 18]
driverWheel = [0X12C, 3]
driverSettings = [0X258, 16]
driverInputs = [0x64, 48]
veichleDynamics = [0x2BC, 40]

# Cooling channel
controlWords = [0x1000, 48]
statusWords = [0x1100, 40]
acknowledgement = [0x1200, 1]

# AMK channel
amkSetpoints1Inverer0 = [0x184, 64]
amkSetpoints1Inverer1 = [0x194, 64]
amkSetpoints1Inverer2 = [0x1A4, 64]
amkSetpoints1Inverer3 = [0x1B4, 64]

amkActualValues1Inverter0 = [0x283, 64]
amkActualValues2Inverter0 = [0x285, 64]
amkActualValues1Inverter1 = [0x293, 64]
amkActualValues2Inverter1 = [0x295, 64]
amkActualValues1Inverter2 = [0x2A3, 64]
amkActualValues2Inverter2 = [0x2A5, 64]
amkActualValues1Inverter3 = [0x2B3, 64]
amkActualValues2Inverter3 = [0x2B3, 64]

