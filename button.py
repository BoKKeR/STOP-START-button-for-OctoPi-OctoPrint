API = "enter octoprint api key"


import RPi.GPIO as GPIO
import time
import json
import requests

headers = {'X-Api-Key': API,"Content-Type":"application/json"}

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(26)
    if input_state == False:
        print('Button Pressed: ')
        time.sleep(0.2)
        url = 'http://127.0.0.1/api/job'
        s = requests.Session()
        r = json.loads((requests.get(url, headers=headers)).content)["state"]
        print r
        if r == "Printing":
                print "Stopping printing"
                contents = json.dumps({"command":"cancel"})
        else:
                print "Starting printing"
                contents = json.dumps({"command":"start"})
        requests.post(url, data=contents, headers=headers)
