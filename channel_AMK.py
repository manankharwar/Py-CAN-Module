import constants as c
from canString import can2A


class AMK(can2A):

    def __init__(self, messageId, dataLength):
        super().__init__(messageId, 500000, False, False, None, dataLength)


class AMKSetPoints1Inverter0(AMK):
    def __init__(self):
        ID = c.amkSetpoints1Inverter0[0]
        dataLen = c.amkSetpoints1Inverter0[1]
        super().__init__(ID, dataLen)

class AMKSetPoints1Inverter1(AMK):
    def __init__(self):
        ID = c.amkSetpoints1Inverter1[0]
        dataLen = c.amkSetpoints1Inverter1[1]
        super().__init__(ID, dataLen)

class AMKSetPoints1Inverter2(AMK):
    def __init__(self):
        ID = c.amkSetpoints1Inverter2[0]
        dataLen = c.amkSetpoints1Inverter2[1]
        super().__init__(ID, dataLen)


class AMKSetPoints1Inverter3(AMK):
    def __init__(self):
        ID = c.amkSetpoints1Inverter3[0]
        dataLen = c.amkSetpoints1Inverter3[1]
        super().__init__(ID, dataLen)


class AMKActualValues1Inverter0(AMK):
    def __init__(self):
        ID = c.amkActualValues1Inverter0[0]
        dataLen = c.amkActualValues1Inverter0[1]
        super().__init__(ID, dataLen)


class AMKActualValues2Inverter0(AMK):
    def __init__(self):
        ID = c.amkActualValues2Inverter0[0]
        dataLen = c.amkActualValues2Inverter0[1]
        super().__init__(ID, dataLen)


class AMKActualValues1Inverter1(AMK):
    def __init__(self):
        ID = c.amkActualValues1Inverter1[0]
        dataLen = c.amkActualValues1Inverter1[1]
        super().__init__(ID, dataLen)


class AMKActualValues2Inverter1(AMK):
    def __init__(self):
        ID = c.amkActualValues2Inverter1[0]
        dataLen = c.amkActualValues2Inverter1[1]
        super().__init__(ID, dataLen)


class AMKActualValues1Inverter2(AMK):
    def __init__(self):
        ID = c.amkActualValues1Inverter2[0]
        dataLen = c.amkActualValues1Inverter2[1]
        super().__init__(ID, dataLen)


class AMKActualValues2Inverter2(AMK):
    def __init__(self):
        ID = c.amkActualValues2Inverter2[0]
        dataLen = c.amkActualValues2Inverter2[1]
        super().__init__(ID, dataLen)


class AMKActualValues1Inverter3(AMK):
    def __init__(self):
        ID = c.amkActualValues1Inverter3[0]
        dataLen = c.amkActualValues1Inverter3[1]
        super().__init__(ID, dataLen)


class AMKActualValues2Inverter3(AMK):
    def __init__(self):
        ID = c.amkActualValues2Inverter3[0]
        dataLen = c.amkActualValues2Inverter3[1]
        super().__init__(ID, dataLen)