#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import sender as sender
import params as params

DO = 29
GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)

def loop():
    status = 1
    tmp = 1
    while True:
        try:
            analogVal = ADC.read(2)
            Vr = 5 * float(analogVal) / 255
            Rt = 10000 * Vr / (5 - Vr)
            temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
            temp = temp - 273.15

            data = {
                'temperature': temp
            }

            sender.send('thermometer', data, False)

            if tmp != status:
                status = tmp
        except Exception as e:
            print e
        time.sleep(params.frequency())

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
