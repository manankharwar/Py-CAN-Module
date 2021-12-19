import can
from can.interface import Bus
import constants as c

class canNode:
    #bus = Bus()

    '''
        interface: String -> interface that represents the CAN interface specified
        channed: String -> CAN channel to be used
        bitrate: Int -> bitrate for CAN communication
    '''
    def __init__(self, interface, bitrate,channel, key):

        if channel == "AMK":
            if key in c.dictAMK:
                self.canString = c.dictAMK[key]()
            else:
                print("Pick a valid key-message pairing from the AMK channel")

        elif channel == "Driver":
            if key in c.dictDriver:
                self.canString = c.dictDriver[key]()
            else:
                print("Pick a valid key-message pairing from the Driver channel")

        elif channel == "Cooling":
            if key in c.dictCooling:
                self.canString = c.dictCooling[key]()
            else:
                print("Pick a valid key-message pairing from the Cooling channel")

        else:
            print("Please enter a valid channel: AMK, Cooling or Driver")

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

        

    def send(self, userData):

        try:
            msg = can.Message(arbitration_id=self.canString.msgId,
                              data=userData,
                              is_extended_id=self.canString.is_extended_id,
                              is_error_frame=self.canString.is_error_frame,
                              is_remote_frame=self.canString.is_remote_frame
                              )
            try:
                self.bus.send(msg)
                print("Message sent on " + str(self.bus.channel_info))
            except:
                print("Message not sent")
        except:
            print("Please ensure message type is initialized")


    def recieve(self):
        while True:
            msg = self.bus.recv()
            print(msg)

