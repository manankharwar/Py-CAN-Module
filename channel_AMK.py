import constants_AMK


class AMK(can2A):
    
    def __init__(self, messageId, dataLength):
        super().__init__(messageId, 500000, False, True, [],dataLength)
    
    
class Dashboard_AccumulatorData(AMK):
    id = constants_AMK.dashAccumulator_Id[0]
    dataLen = constants_AMK.dashAccumulator_Id[1]
    
    def __init__(self):
        super().__init__(id, dataLen)