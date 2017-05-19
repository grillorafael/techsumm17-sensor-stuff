#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import time
import sender as sender
import params as params

# 33 37

Timeout = 2

TRIG = int(sys.argv[1])
ECHO = int(sys.argv[2])
INDEX = sys.argv[3]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def distance():
    print "Getting Reading"
    startTime = time.time()

    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)


    while GPIO.input(ECHO) == 0:
        if time.time() - startTime > Timeout:
            return False
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        if time.time() - startTime > Timeout:
            return False
        a = 1
    time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 * 100

def loop():
    while True:
        try:
            dis = distance()
            print dis
            if dis != False:
                data = {
                    'distance': dis
                }
                sender.send('sonar-{}'.format(INDEX), data, INDEX == 'front')
        except Exception as e:
            print e
        time.sleep(params.frequency())

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
