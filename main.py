import channel_AMK as AMK
import channel_Driver as Driver
import channel_Cooling as Cooling
import constants
import dict
import canNode
import testing

def main():
    '''
    msg1 = Driver.DashboardAccumulatorData()

    msg1.newData([1,2,3,4,5,6])

    msg2 = Cooling.CoolingAcknowledgement()

    try:
        print("msg1")
        print(msg1.msgId)
        print(msg1.dataBits)
        print(msg1.bitrate)
        print(msg1.is_extended_id)
        print(msg1.is_error_frame)
        print(msg1.is_remote_frame)
        print(msg1.data)
        print("\n")

        print("msg2")
        print(msg2.msgId)
        print(msg2.dataBits)
    except:
        pass
        '''

    testing.testRandom()



main()