import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "5glnhi",
        "typeId": "intership",
        "deviceId":"HR1702"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print(" %s" % cmd.data)
    m=cmd.data['command']
    print()
    if(m=="lighton"):
        print("....Light is ON....")
    elif(m=="lightoff"):
        print("....Light is OFF....")
    elif(m=="fanon"):
        print("....Fan is On....")
    elif(m=="fanoff"):
        print("....Fan is OFF....")
    elif(m=="waterpumpon"):
        print("....Water Pump is On....")
    elif(m=="waterpumpoff"):
        print("....Water Pump is OFF....")
    print() 
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,125)
    hum=random.randint(0,100)
    waterlevel=random.randint(0,500)
    myData={'d':{'temperature':temp, 'humidity':hum, 'waterlevel':waterlevel}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    print()
    if temp<30 and hum<30:
        print("Everything is fine")
        if waterlevel<100:
         print("Turn on the Water Pump")
        elif 100<waterlevel<450:
         print("Water level is moderate")
        elif waterlevel>450:
         print("Water level is full")
    elif temp<40 and hum>30:
        print("Entering into danger zone")
        if waterlevel<100:
         print("Turn on the Water Pump")
        elif 100<waterlevel<450:
         print("Water level is moderate")
        elif waterlevel>450:
         print("Water level is full")
    elif temp>40 or waterlevel>450:
        print("Turn on the exhausted fans")
        if waterlevel<100:
         print("Turn on the Water Pump")
        elif 100<waterlevel<450:
         print("Water level is moderate")
        elif waterlevel>450:
         print("Water level is full")
    print()
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
