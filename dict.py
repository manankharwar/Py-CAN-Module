'''
File containing dictionary key classes to be called from main
'''

import channel_AMK
import channel_Cooling
import channel_Driver


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

dictCooling = {
    1: channel_Cooling.CoolingControlWords,
    2: channel_Cooling.CoolingStatusWords,
    3: channel_Cooling.CoolingAcknowledgement
}

dictDriver = {
    1: channel_Driver.DashboardAccumulatorData,
    2: channel_Driver.DashboardMotorData,
    3: channel_Driver.DashboardVehicleData,
    4: channel_Driver.DriverWheelControls,
    5: channel_Driver.DriverDriverSettings,
    6: channel_Driver.DriverDrivingInputs,
    7: channel_Driver.DriverVehicleDynamics
}
