sudo apt-get update
sudo apt-get install build-essential git scons swig python3-pip -y
cd /home/pi/
git clone https://github.com/matt-desmarais/freezeralarm.git
sudo pip3 install adafruit-io RPi.GPIO twilio datetime
cd /home/pi/
git clone https://github.com/adafruit/Adafruit_Python_MAX31855.git
cd Adafruit_Python_MAX31855
sudo python3 setup.py install
cd /home/pi/
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
cd /home/pi/
git clone https://github.com/simonmonk/squid.git
cd squid
sudo python3 setup.py install
