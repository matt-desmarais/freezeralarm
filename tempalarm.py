import time
import math
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from twilio.rest import Client 
import datetime

#Twilio Credentails/setup
numbers_to_message = ['+12345678910']
fromnumber = '+12345678910'
account_sid = 'SID'
auth_token = 'Token'
client = Client(account_sid, auth_token)

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 11
CS  = 9
DO  = 10
sensor = MAX31855.MAX31855(CLK, CS, DO)

tempAlarmThreshold = 20
tempAlarmDuration = 20
textsent = False

print('Press Ctrl-C to quit.')
while True:
    textsent = False
    temp = sensor.readTempC()
    if math.isnan(temp):
        continue
    start = time.time()
    while c_to_f(temp) > tempAlarmThreshold:
        time.sleep(10)
        temp = sensor.readTempC()
        now = time.time()
        elapsed = (now - start)/60
        print('elapsed:'+str(elapsed))
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
    time.sleep(2)
