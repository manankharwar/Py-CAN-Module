import can
from can.interface import Bus

class canNode:
    bus = Bus()

    '''
        interface: String -> interface that represents the CAN interface specified
        channed: String -> CAN channel to be used
        bitrate: Int -> bitrate for CAN communication
    '''
    def __init__(self, interface, channel, bitrate):
        try:
            can.rc['interface'] = interface
        except:
            print("Please enter a correct interface")

        try: 
            can.rc['channel'] = channel
        except:
            print("Please enter a correct channel")

        try:
            can.rc['bitrate'] = bitrate
        except:
            print("Please enter a valid bitrate")
        

    def send(self):
        pass

    def recieve(self):
        pass



    