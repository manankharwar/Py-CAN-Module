import constants as c
from canString import can2A


class AMK(can2A):

    def __init__(self, msgType):
        super().__init__(500000, False, False, msgType)


class AMKSetPoints1Inverter0(AMK):

    def __init__(self):
        super().__init__(c.amkSP1I0)


class AMKSetPoints1Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkSP1I1)


class AMKSetPoints1Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkSetpoints1Inverter2)


class AMKSetPoints1Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkSP1I3)


class AMKActualValues1Inverter0(AMK):
    def __init__(self):
        super().__init__(c.amkAV1I0)


class AMKActualValues2Inverter0(AMK):
    def __init__(self):
        super().__init__(c.amkAV2I0)


class AMKActualValues1Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkAV1I1)


class AMKActualValues2Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkAV2I1)


class AMKActualValues1Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkAV1I2)


class AMKActualValues2Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkAV2I2)


class AMKActualValues1Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkAV1I3)


class AMKActualValues2Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkAV2I3)

