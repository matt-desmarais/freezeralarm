import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY      = 'IO KEY'
ADAFRUIT_IO_USERNAME = 'user name' 

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 11
CS  = 9
DO  = 10
sensor = MAX31855.MAX31855(CLK, CS, DO)

# Loop printing measurements and uploading to IO about every minute
print('Press Ctrl-C to quit.')
while True:
    temp = sensor.readTempC()
    internal = sensor.readInternalC()
    print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
    print('    Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))
    client.connect()
    client.publish('freezer',c_to_f(temp))
    time.sleep(58)
