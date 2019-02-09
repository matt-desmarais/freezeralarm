import time
import math
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from twilio.rest import Client 
import datetime

#Twilio Credentails/setup
numbers_to_message = ['+1234567890']
fromnumber = '+1234567890'
account_sid = 'twilio sid'
auth_token = 'twilio token'
client = Client(account_sid, auth_token)

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 11
CS  = 9
DO  = 10
sensor = MAX31855.MAX31855(CLK, CS, DO)

isnan = False
tempAlarmThreshold = 0
tempAlarmDuration = 20
textsent = False
previousTemp = None

print('Press Ctrl-C to quit.')
while True:
    textsent = False
    temp = sensor.readTempC()
    if math.isnan(temp):
        continue
    if(previousTemp != None and abs(c_to_f(previousTemp)-c_to_f(temp)) > 10):
        print("previous temp error")
        previousTemp = temp
        temp = sensor.readInternalC()
        continue
    start = time.time()
    while c_to_f(temp) > tempAlarmThreshold or math.isnan(temp):
        temp = sensor.readTempC()
        print('first:'+str(c_to_f(temp)))
        if math.isnan(temp):
            print('continued')
            continue
        if(previousTemp != None and abs(c_to_f(previousTemp)-c_to_f(temp)) > 10):
            print("previous temp error")
            previousTemp = temp
            temp = sensor.readTempC()
            continue
        time.sleep(3)
        now = time.time()
        elapsed = (now - start)/60
        print('elapsed:'+str(elapsed)+" Temp: "+str(c_to_f(temp)))
        if elapsed > tempAlarmDuration:
            print('Temperature Alarm')
            if not textsent:
                for number in numbers_to_message:
                                client.messages.create(
                                        body='Freezer Temperature Alarm at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+" It has been over "+str(tempAlarmThreshold) +" Degrees for "+str(tempAlarmDuration)+" minutes and is currently "+str(c_to_f(temp)),
                                        from_=fromnumber,
                                        to=number
                                )
                textsent = True
    internal = sensor.readInternalC()
    print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
    print('    Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))
    previousTemp = temp
    time.sleep(2)
