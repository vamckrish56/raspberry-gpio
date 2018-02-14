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

    state = resp.text

    # Red
    if(state == 'RED'):
        GPIO.output(10,False)
        GPIO.output(11,False)
        GPIO.output(9, True)
        time.sleep(5)

    # Red and amber
    if (state == 'RED-YELLOW'):
        GPIO.output(10, True)
        time.sleep(5)

    # Green
    if (state == 'GREEN'):
        GPIO.output(9, False)
        GPIO.output(10, False)
        GPIO.output(11, True)
        time.sleep(5)

    # Amber
    if (state == 'YELLOW'):
        GPIO.output(11, False)
        GPIO.output(9, False)
        GPIO.output(10, True)
        time.sleep(5)
