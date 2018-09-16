# freezeralarm
pi zero w based freezer alarm with sms

Easy way to install the dependencies and freezeralarm repo <br/>
curl https://raw.githubusercontent.com/matt-desmarais/freezeralarm/master/install.sh | bash <br/>

Single Door Alarm <br/>
Use singledooralarm.py <br/>
Connect the buzzer <br/>
Connect Pi 3.3V to Buzzer + <br/>
Connect Pi Pin 17 to Buzzer – <br/>
Connect Pi Ground to Buzzer N <br/>

Connect the door sensor, doesn't matter which wire goes where <br/>
attach one wire to Pi Ground <br/>
attach the other wire to Pi Pin 18 <br/>

Connect the LED <br/>
attach Pi Ground to black wire <br/>
attach Pi Pin 16 to the red wire <br/>
attach Pi Pin 20 to the green wire <br/>
attach Pi Pin 21 to the blue wire <br/>
![wiringdiagramsingledooor](https://github.com/matt-desmarais/freezeralarm/raw/master/singledoordiagram.png)

Double Door Alarm <br/>
Use doubledooralarm.py <br/>
Connect the buzzer <br/>
Connect Pi 3.3V to Buzzer + <br/>
Connect Pi Pin 17 to Buzzer – <br/>
Connect Pi Ground to Buzzer N <br/>

Connect the door sensors, doesn't matter which wire goes where <br/>
Attach the first door sensor <br/>
attach one wire to Pi Ground <br/>
attach the other wire to Pi Pin 18 <br/>
Attach the second door sensor <br/>
attach one wire to Pi Ground <br/>
attach the other wire to Pi Pin 27 <br/>

Connect the LEDs <br/>
attach Pi Ground to black wire <br/>
attach Pi Pin 16 to the red wire <br/>
attach Pi Pin 20 to the green wire <br/>
attach Pi Pin 21 to the blue wire <br/>

attach Pi Ground to black wire <br/>
attach Pi Pin 13 to the red wire <br/>
attach Pi Pin 19 to the green wire <br/>
attach Pi Pin 26 to the blue wire <br/>
![wiringdiagramdoubledooor](https://github.com/matt-desmarais/freezeralarm/raw/master/doubledoordiagram.png)

Temperature Monitoring <br/>
Use tempiodata.py <br/>
Connect the MAX31855  <br/>
Connect Pi 3.3V to MAX31855 Vin <br/>
Connect Pi GND to MAX31855 GND <br/>
Connect Pi GPIO 10 to MAX31855 DO. <br/>
Connect Pi GPIO 9 to MAX31855 CS. <br/>
Connect Pi GPIO 11 to MAX31855 CLK. <br/>
![wiringdiagramMAX31855](https://github.com/matt-desmarais/freezeralarm/raw/master/tempdiagram.png) <br/>

Parts List: <br/>
[Pi Zero W - $10](https://www.adafruit.com/product/3400) <br/>
[Header pins - $1](https://www.adafruit.com/product/2822) <br/>
[F/F jumper wires 3" - $4](https://www.adafruit.com/product/794) <br/>
[F/F jumper wires 12" - $8](https://www.adafruit.com/product/793) <br/>
[Squid LEDs - $10 (2 count)](https://www.amazon.com/Monk-Makes-SKU00044-Raspberry-Squid/dp/B0170C8ITK/) or [Squid LED - $4 (single)]()<br/>
[Active Piezo Buzzer - $5 (5 count)](https://www.amazon.com/gp/product/B076SXP7VJ/) <br/>
[Magnetic Door Switch(s) - $4 each](https://www.adafruit.com/product/375) <br/>
[MAX31855 - $15](https://www.adafruit.com/product/269) <br/>
[Thermocouple - $10](https://www.adafruit.com/product/3245)
