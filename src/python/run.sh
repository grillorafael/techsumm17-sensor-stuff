#!/bin/sh

nohup python thermometer.py > thermometer.out &
nohup python photoresistor.py > photon.out &

nohup python sonar.py 35 37 front > sfront.out &
nohup python sonar.py 38 40 left > sleft.out &
nohup python sonar.py 32 36 right > sright.out &
