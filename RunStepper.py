from Stepper import Stepper
import time,requests

# initialize GPIO17,GPIO22,GPI23,GPI24
stepper = Stepper(17, 22, 23, 24)
# Total number of steps in one revolution = 3200
revolution = int(3200)
steps = int(0)

waitDelay = int(10)
hold = int(5)

try:
    while True:
        print 'hello - getting cpu and memory'
        cpureq = requests.get('http://localhost:5000/app/teamcity/builds/buildType:(id:cpumotor),branch:develop')
        memoryreq = requests.get('http://localhost:5000/app/teamcity/builds/buildType:(id:memorymotor),branch:develop')

        cpu = int(cpureq.text)
        memory = int(memoryreq.text)
        print cpu
        new_steps = cpu*revolution/100
        print new_steps

        if new_steps >= steps:
            stepper.rotate_clockwise(new_steps-steps,True)
            time.sleep(waitDelay)
        else:
            stepper.rotate_counterwise(steps-new_steps,True)
            time.sleep(waitDelay)
        steps = new_steps
except KeyboardInterrupt:
    stepper.cleanup()
