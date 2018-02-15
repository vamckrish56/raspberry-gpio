from Stepper import Stepper
import time

# initialize GPIO17,GPIO22,GPI23,GPI24
stepper = Stepper(17, 22, 23, 24)
# number of steps
steps = 1000

waitDelay = 10
hold = 5

try:
    while True:
        stepper.rotate_clockwise(steps,True)
        time.sleep(waitDelay)
        stepper.rotate_counterwise(steps,True)
except KeyboardInterrupt:
    stepper.cleanup()
