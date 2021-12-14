import can
from can import bus
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
        

    def send(self, msg):
        #msg = can.Message(arbitration_id=)

        try:
            bus.send(msg)
            print("Message sent on " + str(bus.channel_info))
        except:
            print("Message not sent")


    def recieve(self):
        while True:
            msg = bus.recv()
            print(msg)


    