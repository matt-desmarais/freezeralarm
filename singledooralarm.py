from twilio.rest import Client 
from time import sleep
import time
import RPi.GPIO as GPIO
from squid import *
import datetime

#Twilio credentials
numbers_to_message = ['+12345678910']
fromnumber = '+12345678910'
account_sid = 'Twilio SID'
auth_token = 'Twilio Token'
client = Client(account_sid, auth_token)

rgb = Squid(16, 20, 21) 
GPIO.setmode(GPIO.BCM)

BuzzerPin = 17 
door_switch_pin = 18
 
#Set up inputs
GPIO.setup(door_switch_pin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)
GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.output(BuzzerPin, GPIO.HIGH)

prev_door = False
start = None
now = None
alarm = False
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
    if not door and prev_door:
        print("door closed")
    #detect if door is closed then turn led blue and 
    #if alarm went off send a closed door sms
    if not door and not prev_door:
                #print("door closed")
                rgb.set_color(BLUE)
                off()
                #time.sleep(2)
                #if alarm has been triggered send text that door has closed
                if alarm:
                        for number in numbers_to_message:
                                client.messages.create(
                                        body = 'Door Closed on freezer at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                                        from_ = fromnumber,
                                        to = number
                                )
                alarm = False
                textsent = False
                resolvedtext = False
                time.sleep(1)
    #detect if door has been opened 
    #if door opened start timer turn led green
    if door and not prev_door:
            print("door opened")
            rgb.set_color(GREEN)
            start = time.time()
            #time.sleep(2)
    #detect if door is still opened 
    #if alarm has been triggered send sms
    if door and prev_door:
            #print("door still open")
            now = time.time()
            time.sleep(1)
            elapsed = (now - start)/60
            if alarm and not textsent:
                    for number in numbers_to_message:
                            client.messages.create(
                            body='Freezer Door Alarm at '+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
                            from_=fromnumber,
                            to=number
                        )
                    textsent = True
            #if 5min passed, activate alarm/sms
            if elapsed > 5:
                on()
                rgb.set_color(RED)
                alarm = True
                continue
            #if 4min passed, flash led red and beep
            if elapsed > 4:
                beep(0.5)
                rgb.set_color(RED)
                time.sleep(1)
                rgb.set_color(OFF)
                continue
            #if 3 min passed, flash led green
            if elapsed > 3:
                rgb.set_color(GREEN)
                time.sleep(1)
                rgb.set_color(OFF)
                time.sleep(1)
    prev_door = door  
