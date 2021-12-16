import constants as c
from canString import can2A


class Cooling(can2A):

    def __init__(self, messageId, dataLength):
        super().__init__(messageId, 500000, False, True, None, dataLength)


class CoolingControlWords(Cooling):
    def __init__(self):
        ID = c.controlWords[0]
        dataLen = c.controlWords[1]
        super().__init__(ID, dataLen)


class CoolingStatusWords(Cooling):
    def __init__(self):
        ID = c.statusWords[0]
        dataLen = c.statusWords[1]
        super().__init__(ID, dataLen)


class CoolingAcknowledgement(Cooling):
    def __init__(self):
        ID = c.acknowledgement[0]
        dataLen = c.acknowledgement[1]
        super().__init__(ID, dataLen)


