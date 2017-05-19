import json
import urllib2
import time
import requests
import params as params
from datetime import date

iteration = 0

url = 'http://team6api.azurewebsites.net/api/car/sensor'
headers = {'content-type': 'application/json'}

def send(sensor, data, storeToFile = False):
    global iteration
    data['createdAt'] = int(round(time.time() * 1000))
    payload = {
        'SensorID': sensor,
        'Message': '{}'.format(json.dumps(data))
    }

    if storeToFile:
        file = open('/tmp/{}'.format(sensor), 'w')
        file.write('{}'.format(json.dumps(payload)))

    iteration += 1

    if iteration % params.sendToAPIEvery() == 0:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print "Sensor sent data: [{} - {}] with result {}".format(sensor, payload, response.status_code)
