from Stepper import Stepper
import time,requests

# initialize GPIO17,GPIO22,GPI23,GPI24
cpuStepper = Stepper(17, 22, 23, 24)
memoryStepper = Stepper(6, 13, 19, 26)
# Total number of steps in one revolution = 3200
revolution = int(3200)
cpusteps = int(0)
cpu_new_steps = int(0)
memorysteps = int(0)
memory_new_steps = int(0)
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
        print memory

        cpu_new_steps = cpu * revolution / 100
        memory_new_steps = memory * revolution / 100

        print cpu_new_steps

        if cpu_new_steps >= cpusteps:
            cpuStepper.rotate_clockwise(cpu_new_steps - cpusteps, True)
        else:
            cpuStepper.rotate_counterwise(cpusteps - cpu_new_steps, True)

        if memory_new_steps >= memorysteps:
            memoryStepper.rotate_clockwise(memory_new_steps - memorysteps, True)
        else:
            memoryStepper.rotate_counterwise(memorysteps - memory_new_steps, True)

        time.sleep(waitDelay)
        cpusteps = cpu_new_steps
        memorysteps = memory_new_steps
# finally reset speedometer to 0 and cleanup
except KeyboardInterrupt:
    cpuStepper.rotate_counterwise(cpu_new_steps, True)
    memoryStepper.rotate_counterwise(memory_new_steps,True)
    cpuStepper.cleanup()
    memoryStepper.cleanup()
