import constants as c
from canString import can2A

#Cooling channel require 500 000 bit/s
class Cooling(can2A):

    def __init__(self, msgType):
        super().__init__(500000, False, False, msgType)


class CoolingControlWords(Cooling):

    def __init__(self):
        super().__init__(c.controlWords)


class CoolingStatusWords(Cooling):

    def __init__(self):
        super().__init__(c.statusWords)


class CoolingAcknowledgement(Cooling):

    def __init__(self):
        super().__init__(c.acknowledgement)


