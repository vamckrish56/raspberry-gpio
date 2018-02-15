import RPi.GPIO as gpio
import time

PINS = [17, 22, 23, 24]
SEQA = [(17,),(22,),(23,),(24,)]

DELAY = 0.05

gpio.setmode(gpio.BCM)
for pin in PINS:
    gpio.setup(pin, gpio.OUT)


def stepper(sequence, pins):
    for step in sequence:
        for pin in pins:
            if pin in step:
                gpio.output(pin, gpio.HIGH)
            else:
                gpio.output(pin, gpio.LOW)
        time.sleep(DELAY)


try:
    while True:
        for _ in range(512):
            stepper(SEQA, PINS)
        for _ in range(512):
            stepper(SEQA[::-1], PINS)
except KeyboardInterrupt:
    gpio.cleanup()