import channel_AMK as AMK
import channel_Driver as Driver
import channel_Cooling as Cooling

def main():
    msg1 = Driver.DashboardAccumulatorData()

    msg1.newData([1,2,3,4,5,6])
    try:
        print(msg1.msgId)
        print(msg1.dataBits)
        print(msg1.bitrate)
        print(msg1.is_extended_id)
        print(msg1.is_error_frame)
        print(msg1.is_remote_frame)
        print(msg1.data)
    except:
        pass

main()