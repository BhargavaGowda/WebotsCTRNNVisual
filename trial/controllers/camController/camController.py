"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from turtle import left
from controller import Robot
from PyCTRNN import CTRNN
import numpy
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


brain = CTRNN(4)

cam = robot.getDevice("camera")
cam.enable(timestep)
leftMotor = robot.getDevice("leftMotor")
rightMotor = robot.getDevice("rightMotor")
leftMotor.setPosition(float("inf"))
rightMotor.setPosition(float("inf"))

# brain.weights = numpy.zeros((brain.size,brain.size))
# brain.bias = numpy.zeros(brain.size)

# brain.weights[2,0] = 4
# brain.weights[3,1] = 4
# brain.weights[2,1] = -4
# brain.weights[3,0] = -4

print(brain.weights)

mutateTimer=0

while robot.step(timestep) != -1:

    if(mutateTimer > 100000):
        brain.mutate(0.5)
        mutateTimer = 0
        print(brain.weights)
    else:
        mutateTimer += timestep
    sensorInput = numpy.array([0,0,0,0])

    brainOutput = brain.step(sensorInput)
   
   
    leftMotor.setVelocity(5*brainOutput[2])
    rightMotor.setVelocity(5*brainOutput[3])
   #print(brainOutput)
   

# Enter here exit cleanup code.
