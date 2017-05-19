#!/bin/sh

nohup python thermometer.py &
nohup python photoresistor.py &

nohup python sonar.py 33 37 front &
nohup python sonar.py 38 40 back &
