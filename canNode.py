import can
from can.interface import Bus
import dict
import time
import random

class canNode:
    bus = Bus()

    '''
        interface: String -> interface that represents the CAN interface specified
        channed: String -> CAN channel to be used
        bitrate: Int -> bitrate for CAN communication
    '''
    def __init__(self, interface, bitrate,channel, key):

        if channel == "AMK":
            if key in dict.dictAMK:
                self.canString = dict.dictAMK[key]()
            else:
                print("Pick a valid key-message pairing from the AMK channel")
                return

        elif channel == "Driver":
            if key in dict.dictDriver:
                self.canString = dict.dictDriver[key]()
            else:
                print("Pick a valid key-message pairing from the Driver channel")
                return

        elif channel == "Cooling":
            if key in dict.dictCooling:
                self.canString = dict.dictCooling[key]()
            else:
                print("Pick a valid key-message pairing from the Cooling channel")
                return

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
            can.rc['bitrate'] = self.canString.bitrate
        except:
            print("Please ensure a proper message was initialized")

        
    # Function to send a single message userData
    def sendSingleton(self, userData):

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

    # Function to send random messages for the given time and interval
    def sendRandom(self, secs, interval):
        tEnd = time.time() + secs
        while time.time() < tEnd:
            self.sendSingleton(self.randomDataGenerator())
            time.sleep(secs/interval)

    # do whatever you do


    def recieve(self):
        while True:
            msg = self.bus.recv()
            print(msg)

    def randomDataGenerator(self):
        data = []
        for i in range(self.canString.dataBits):
            data.append(random.randint(-255,256))
        return data
