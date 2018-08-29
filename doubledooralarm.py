#!/usr/bin/env python
from twilio.rest import Client 
from time import sleep
import time
import RPi.GPIO as GPIO
from squid import *
import datetime

numbers_to_message = ['+12345678910']
fromnumber = '+12345678910'
account_sid = 'Twilio SID'
auth_token = 'Twilio Token'
client = Client(account_sid, auth_token)

rgb = Squid(16, 20, 21) 
GPIO.setmode(GPIO.BCM)

BuzzerPin = 17 
door_switch_pin = 18
door_switch_pin2 = 27

#Set up inputs
GPIO.setup(door_switch_pin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)
GPIO.setup(door_switch_pin2, GPIO.IN,  pull_up_down=GPIO.PUD_UP)
GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.output(BuzzerPin, GPIO.HIGH)

prev_door = False
prev_door2 = False
start = None
start2 = None
now = None
alarm = False
alarm2 = False
textsent = False
resolvedtext = False

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

#main loop
while True:
	#Update sensor state each loop
	door = GPIO.input(door_switch_pin)
	door2 = GPIO.input(door_switch_pin2)
        if not door and not prev_door and not door2 and not prev_door2:
                print "doors closed"
                rgb.set_color(BLUE)
                off()
                #time.sleep(2)
                #if alarm has been triggered send text that door has closed
                if alarm:
                        for number in numbers_to_message:
                                client.messages.create(
                                        body = 'Door Closed, freezer ONE at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                                        from_ = fromnumber,
                                        to = number
                                )
                if alarm2:
                        for number in numbers_to_message:
                                client.messages.create(
                                        body = 'Door Closed, freezer TWO at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                                        from_ = fromnumber,
                                        to = number
                                )
                alarm = False
                alarm2 = False
                textsent = False
                resolvedtext = False
        if door and not prev_door:
		print "door one opened"
                rgb.set_color(GREEN)
		start = time.time()
                #time.sleep(2)
        if door2 and not prev_door2:
                print "door two opened"
                rgb.set_color(GREEN)
                start2 = time.time()
                #time.sleep(2)
	if door and prev_door:
		print "door one still open"
		now = time.time()
                time.sleep(2)
		elapsed = (now - start)/60
                if alarm and not textsent:
                        for number in numbers_to_message:
                                client.messages.create(
                                        body='Freezer Door Alarm on ONE at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                                        from_=fromnumber,
                                        to=number
                                )
                        textsent = True
                if elapsed > 5:
                        on()
                        rgb.set_color(RED)
			alarm = True
                        continue
		if elapsed > 4:
                        beep(0.5)
			rgb.set_color(RED)
			time.sleep(1)
			rgb.set_color(OFF)
                        continue
		if elapsed > 3:
                        rgb.set_color(GREEN)
                        time.sleep(1)
                        rgb.set_color(OFF)
        if door2 and prev_door2:
                print "door two still open"
                now = time.time()
                #time.sleep(2)
                elapsed = (now - start)/60
                if alarm and not textsent:
                        for number in numbers_to_message:
                                client.messages.create(
                                        body='Freezer Door Alarm on TWO at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                                        from_=fromnumber,
                                        to=number
                                )
                        textsent = True
                if elapsed > 5:
                        on()
                        rgb.set_color(RED)
                        alarm = True
                        continue
                if elapsed > 4:
                        beep(0.5)
                        rgb.set_color(RED)
                        time.sleep(1)
                        rgb.set_color(OFF)
                        continue
                if elapsed > 3:
                        rgb.set_color(GREEN)
                        time.sleep(1)
                        rgb.set_color(OFF)
        prev_door = door    
