# freezeralarm
pi zero w based freezer alarm with sms

Single Door Alarm <br/>
Use singledooralarm.py <br/>
Connect the buzzer <br/>
Connect Pi 3.3V to Buzzer + <br/>
Connect Pi Pin 17 to Buzzer – <br/>
Connect Pi Ground to Buzzer N <br/>

Connect the door sensor, doesn't matter which wire goes where <br/>
attach one wire to Pi Ground <br/>
attach the other wire to Pi Pin 18 <br/>

Connect the LED
attach Pi Ground to black wire
attach Pi Pin 16 to the red wire
attach Pi Pin 20 to the green wire
attach Pi Pin 21 to the blue wire
![wiringdiagramsingledooor](https://github.com/matt-desmarais/freezeralarm/raw/master/singledoordiagram.png)

Double Door Alarm <br/>
Use doubledooralarm.py <br/>
Connect the buzzer
Connect Pi 3.3V to Buzzer +
Connect Pi Pin 17 to Buzzer –
Connect Pi Ground to Buzzer N

Connect the door sensors, doesn't matter which wire goes where
Attach the first door sensor
attach one wire to Pi Ground
attach the other wire to Pi Pin 18
Attach the second door sensor
attach one wire to Pi Ground
attach the other wire to Pi Pin 27

Connect the LEDs
attach Pi Ground to black wire
attach Pi Pin 16 to the red wire
attach Pi Pin 20 to the green wire
attach Pi Pin 21 to the blue wire

attach Pi Ground to black wire
attach Pi Pin 13 to the red wire
attach Pi Pin 19 to the green wire
attach Pi Pin 26 to the blue wire
![wiringdiagramdoubledooor](https://github.com/matt-desmarais/freezeralarm/raw/master/doubledoordiagram.png)

Temperature Monitoring <br/>
Use tempiodata.py <br/>
![wiringdiagramMAX31855](https://github.com/matt-desmarais/freezeralarm/raw/master/tempdiagram.png) <br/>
Parts List: <br/>
[Pi Zero W - $10](https://www.adafruit.com/product/3400) <br/>
[Squid LED - $10 (2 count)](https://www.amazon.com/Monk-Makes-SKU00044-Raspberry-Squid/dp/B0170C8ITK/) <br/>
[Active Piezo Buzzer - $5 (5 count)](https://www.amazon.com/gp/product/B076SXP7VJ/) <br/>
[Magnetic Door Switch(s) - $4 each](https://www.adafruit.com/product/375) <br/>
[MAX31855 - $15](https://www.adafruit.com/product/269) <br/>
[Thermocouple - $10](https://www.adafruit.com/product/3245)
