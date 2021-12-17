import channel_AMK as AMK
import channel_Driver as Driver
import channel_Cooling as Cooling

def main():
    msg1 = Driver.DashboardAccumulatorData([1,255,3,4,5])
    msg2 = AMK.AMKActualValues1Inverter0([1,2,3,4,5,6,7])
    try:
        print(msg1.msgId)
        print(msg1.dataLength)
        print(msg1.data)
    except:
        pass

main()