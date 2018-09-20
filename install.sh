sudo apt-get update
sudo apt-get install build-essential python-dev python-pip python-smbus git scons swig python3-pip -y
sudo pip install twilio
sudo pip uninstall pyopenssl -y
sudo apt-get install python-openssl
sudo pip install datetime
git clone https://github.com/simonmonk/squid.git
cd squid
sudo python setup.py install
cd /home/pi/
git clone https://github.com/matt-desmarais/freezeralarm.git
sudo pip3 install adafruit-io RPi.GPIO twilio
cd /home/pi/
git clone https://github.com/adafruit/Adafruit_Python_MAX31855.git
cd Adafruit_Python_MAX31855
sudo python3 setup.py install
cd /home/pi/
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
