import constants as c
from canString import can2A


class Cooling(can2A):

    def __init__(self, messageId, dataLength, data):
        super().__init__(messageId, 500000, False, False, data, dataLength)


class CoolingControlWords(Cooling):
    def __init__(self, data):
        ID = c.controlWords[0]
        dataLen = c.controlWords[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


class CoolingStatusWords(Cooling):
    def __init__(self, data):
        ID = c.statusWords[0]
        dataLen = c.statusWords[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


class CoolingAcknowledgement(Cooling):
    def __init__(self, data):
        ID = c.acknowledgement[0]
        dataLen = c.acknowledgement[1]
        if self.checkDataLen(data, dataLen):
            super().__init__(ID, dataLen, data)
        else:
            print("Could not build message! Improper data passed")


