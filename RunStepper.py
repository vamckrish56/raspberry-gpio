import Stepper
import time

# initialize GPIO17,GPIO22,GPI23,GPI24
stepper = Stepper(17, 22, 23, 24)
# number of steps
steps = 165

try:
    while True:
        stepper.rotate_clockwise(steps)
        time.sleep(5)
        stepper.rotate_counterwise(steps)
except KeyboardInterrupt:
    stepper.cleanup()
