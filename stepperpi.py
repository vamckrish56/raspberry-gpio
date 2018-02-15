import RPi.GPIO as gpio
import time

PINS = [22,21,18,17]
SEQA = [(22,),(21,),(18,),(17,)]

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