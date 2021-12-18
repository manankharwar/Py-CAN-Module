import constants as c
from canString import can2A


class AMK(can2A):

    def __init__(self, msgType):
        super().__init__(500000, False, False, msgType)


class AMKSetPoints1Inverter0(AMK):

    def __init__(self):
        super().__init__(c.amkSetpoints1Inverter0)


class AMKSetPoints1Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkSetpoints1Inverter1)


class AMKSetPoints1Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkSetpoints1Inverter2)


class AMKSetPoints1Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkSetpoints1Inverter3)


class AMKActualValues1Inverter0(AMK):
    def __init__(self):
        super().__init__(c.amkActualValues1Inverter0)


class AMKActualValues2Inverter0(AMK):
    def __init__(self):
        super().__init__(c.amkActualValues2Inverter0)


class AMKActualValues1Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues1Inverter1)


class AMKActualValues2Inverter1(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues2Inverter1)


class AMKActualValues1Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues1Inverter2)


class AMKActualValues2Inverter2(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues2Inverter2)


class AMKActualValues1Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues1Inverter3)


class AMKActualValues2Inverter3(AMK):

    def __init__(self):
        super().__init__(c.amkActualValues2Inverter3)
