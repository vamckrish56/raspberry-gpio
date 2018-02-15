import RPi.GPIO as GPIO
import time
import signal
import sys
import requests

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
    print 'hello'
    resp = requests.get('http://localhost:5000/app/teamcity/builds/buildType:(id:uds),branch:develop')
    uat_resp = requests.get('http://localhost:5000/app/teamcity/builds/buildType:(id:uds),branch:develop')

    state = resp.text
    uat_state = uat_resp.text

    # Red
    if(state == 'RED'):
        GPIO.output(10,False)
        GPIO.output(11,False)
        GPIO.output(9, True)

    # Green
    if (state == 'GREEN'):
        GPIO.output(9, False)
        GPIO.output(10, False)
        GPIO.output(11, True)

    # Amber
    if (state == 'YELLOW'):
        GPIO.output(11, False)
        GPIO.output(9, False)
        GPIO.output(10, True)

    # Red
    if(state == 'RED'):
        GPIO.output(16,False)
        GPIO.output(20,False)
        GPIO.output(21, True)

    # Green
    if (state == 'GREEN'):
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)

    # Amber
    if (state == 'YELLOW'):
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)

    time.sleep(5)
