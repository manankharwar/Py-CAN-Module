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


    n = canNode.canNode('i',"Cooling",100)

    #testing.testRandom()

    '''

    #printFullKey()
    run()


def run():
    chan = input("Enter a channel: AMK, Cooling or Driver: ")
    if chan == "AMK":
        printAMK()
        key = getKey()
        if key not in dict.dictAMK:
            print("That is an incorrect key please try again")
            run()
    elif chan == "Cooling":
        printCooling()
        key = getKey()
        if key not in dict.dictCooling:
            print("That is an incorrect key please try again")
            run()
    elif chan == "Driver":
        printDriver()
        key = getKey()
        if key not in dict.dictDriver:
            print("That is an incorrect key please try again")
            run()
    else:
        print("That is an incorrect channel please try again")
        run()

    #Add control flow for code for constant messaging
    node = canNode.canNode('blank', chan, key)

def getKey():
    return int(input("Now enter the corresponding key to descriptions above\n"))

def printFullKey():
    print("Welcome to CAN node emulator using Raspberry Pi!\n"
          "The user must input the corresponding channel and key as listed below\n"
          "Channel | Key | Description\n"
          "\n")
    printAMK()
    printCooling()
    printDriver()

def printCooling():
    print(
        "        | Key | Description\n"
        "Cooling | 1 | Cooling Control Words\n"
          "Cooling | 2 | Cooling Status Words\n"
          "Cooling | 3 | Acknowledgement\n"
          "\n")

def printAMK():
    print( 
    "    | Key | Description\n"
    "AMK | 1 | AMK Set Points 1 Inverter 0\n"
    "AMK | 2 | AMK Set Points 1 Inverter 1\n"
    "AMK | 3 | AMK Set Points 1 Inverter 2\n"
    "AMK | 4 | AMK Set Points 1 Inverter 3\n"
    "AMK | 5 | AMK Actual Values 1 Inverter 0\n"
    "AMK | 6 | AMK Actual Values 2 Inverter 0\n"
    "AMK | 7 | AMK Actual Values 1 Inverter 1\n"
    "AMK | 8 | AMK Actual Values 2 Inverter 1\n"
    "AMK | 9 | AMK Actual Values 1 Inverter 2\n"
    "AMK | 10 | AMK Actual Values 2 Inverter 2\n"
    "AMK | 11 | AMK Actual Values 1 Inverter 3\n"
    "AMK | 12 | AMK Actual Values 2 Inverter 3\n"
    "\n")

def printDriver():
    print(
        "       | Key | Description\n"
        "Driver | 1 | Dashboard - Accumulator Data\n"
        "Driver | 2 | Dashboard - Motor Data\n"
        "Driver | 3 | Dashboard - Vehicle Data\n"
        "Driver | 4 | Driver - Wheel Controls\n"
        "Driver | 5 | Driver - Driver Settings\n"
        "Driver | 6 | Driver - Driver Inputs\n"
        "Driver | 7 | Vehicle Dynamics - GPS\n"
        "\n")

main()