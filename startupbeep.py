from time import sleep
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BuzzerPin = 17 

GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.output(BuzzerPin, GPIO.HIGH)

#turn buzzer on
def on():
	GPIO.output(BuzzerPin, GPIO.LOW)

#turn buzzer off
def off():
	GPIO.output(BuzzerPin, GPIO.HIGH)

#beep sequence
def beep(x):
	on()
	time.sleep(x)
	off()
	time.sleep(x)

beep(.2)
beep(.2)
beep(.2)
beep(.2)
beep(.2)
