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
leftTouchSensor = robot.getDevice("leftTouchSensor")
rightTouchSensor = robot.getDevice("rightTouchSensor")
leftTouchSensor.enable(timestep)
rightTouchSensor.enable(timestep)
leftMotor = robot.getDevice("leftMotor")
rightMotor = robot.getDevice("rightMotor")
leftMotor.setPosition(float("inf"))
rightMotor.setPosition(float("inf"))
leftMotorLed = robot.getDevice("leftMotorIndicator")
rightMotorLed = robot.getDevice("rightMotorIndicator")

# brain.weights = numpy.zeros((brain.size,brain.size))
# brain.bias = numpy.zeros(brain.size)

# brain.weights[2,0] = 4
# brain.weights[3,1] = 4
# brain.weights[2,1] = -4
# brain.weights[3,0] = -4



while robot.step(timestep) != -1:

    rightMotorVel = 5
    leftMotorVel = 5
   
    leftMotor.setVelocity(leftMotorVel)
    rightMotor.setVelocity(rightMotorVel)

    leftMotorLed.set(int(abs(255*leftMotor.getVelocity()/leftMotor.getMaxVelocity())))
    rightMotorLed.set(int(abs(255*rightMotor.getVelocity()/rightMotor.getMaxVelocity())))
   #print(brainOutput)
   

# Enter here exit cleanup code.
