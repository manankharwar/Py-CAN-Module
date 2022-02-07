'''
    This is a class to represent the different types of CAN
    string messages that canNode will utilize to 
    communicate with other hardware.
'''
class canString:
    
    #can2.0A id length is 11 bits 
    #can2.0B id length is 29 bits and has the flag `is_extended_id` when passing a message
    msgId = ""

    bitrate = 0

    # bool representing error frame flag
    # occures when a node detects an error in a
    # message which should casue other nodes to send an error frame as well
    is_error_frame = False

    # bool representing remote frame flag
    # solicit data from other nodes by not passing nay data?
    is_remote_frame = False
    
    is_extended_id = False

    data = []

    dataBits = 0

    def __init__(self, bitRate, errorFrame, remoteFrame, extendedId, msgType):
        self.msgId = msgType[0]
        self.bitrate = bitRate
        self.is_remote_frame = errorFrame
        self.is_remote_frame = remoteFrame
        self.is_extended_id = extendedId
        self.dataBits = msgType[1]

    #check length of hexidecimal string for different can nodes

    def checkHexLen(self, string):
        bits = 0
        for ch in string[2:]:
            #A to Z or a to z
            if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
                bits += 4

            #0 to 9
            elif (ord(ch) >= 48 and ord(ch) <= 57):
                bits += 1
            else:
                return ValueError("Please enter a correct id")
        return bits

    #check that data being passed is of proper size and each element is 8 bytes or less
    def checkDataLen(self, lst, bits):
        bitCount = 0
    
        #check to make sure that max data size of 8 bits per item is not larger than total bits
        if len(lst) > bits/8:
            return False
        else:
            for item in lst:
                #get length of item in bits
                dataLen = self.checkHexLen(bin(item))
                
                if dataLen > 8:
                    return False
                bitCount += dataLen
                
            #check that bitcount less than or equal to bits passed
            if bitCount <= bits:
                return True
            return False

    def newData(self, Data):
        if self.checkDataLen(Data, self.dataBits):
            self.data = Data
        else:
            print("Please add proper data")

class can2A(canString):

    def __init__(self, bitRate, errorFrame, remoteFrame, msgType):
        #initialize flags for incorrect protocol requirements
        flag_id = False
        flag_bitRate = False
        if self.checkHexLen(str(msgType[0])) > 11:
            print("Please enter a valid message ID for can2.0A protocol")
            flag_id = True
        
        if bitRate != 500000:
            print("Please enter a valid bitrate for can2.0A protocol")
            flag_bitRate = True
        
        if flag_id or flag_bitRate:
            print("Did not complete node build")
        else:
            super().__init__(bitRate, errorFrame, remoteFrame, False, msgType)
            print("Built node")  

'''
class can2B(canString):
    
    def __init__(self, id, bitRate, errorFrame, remoteFrame,data, dataLen):
        flag_id = False
        flag_bitRate = False
        if canString.checkHexLen(id) > 29:
            print("Please enter a valid message ID for can2.0B protocol")
            lenFlag = True
        
        if bitRate != 1000000:
            print("Please enter a valid bitrate for can2.0B protocol")
            flag_bitRate = True
        
        if flag_id == True or flag_bitRate == True:
            print("Did not complete node build")
        else:
            super().__init__(id, bitRate, errorFrame, remoteFrame, True, data, dataLen)
            print("Built node")  
'''
        
    