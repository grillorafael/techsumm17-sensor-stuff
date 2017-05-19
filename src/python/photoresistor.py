#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import sender as sender
import params as params

DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)


def loop():
	global iteration
	status = 1
	while True:
		value = ADC.read(0)
		data = {
			'reading': value
		}
		sender.send('photoresistor', data)
		time.sleep(params.frequency())

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		pass
