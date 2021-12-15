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

    #bool representing error frame flag
    is_error_frame = False

    #bool representing remote frame flag
    is_remote_frame = True
    
    def __init__(self, id, bitRate, errorFrame, remoteFrame):
        self.msgId = id
        self.bitrate = bitRate
        self.errorFrame = errorFrame
        self.remoteFrame = remoteFrame

    #check length of hexidecimal string for different can nodes
    def checkHexLen(string):
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


class can2A(canString):

    def __init__(self, id, bitRate, errorFrame, remoteFrame):
        flag = False
        if canString.checkHexLen(id) > 11:
            return ValueError("Please enter a valid message ID for can2.0A protocol")
        
        if bitRate != 500000:
            return ValueError("Please enter a valid bitrate for can2.0A protocol")
        
        super().__init__(id, bitRate, errorFrame, remoteFrame)
        print("Built node")

