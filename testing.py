import dict
import channel_Driver as driver
import channel_AMK as amk
import channel_Cooling as cooling

# Function that builds all possible channel configurations
def testAll():

    for i in range(1,13):
        print(dict.dictAMK[i]().msgId)

    for i in range(1,4):
        print(dict.dictCooling[i]().msgId)

    for i in range(1,8):
        print(dict.dictDriver[i]().msgId)

#Function that randomly chooses a channel and sends a random amount of data
def testRandom():

    test = cooling.CoolingControlWords()

    print(test.msgId)

    test.newData([1,2,3,4,5])

    print(test.data)