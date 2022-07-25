"""simpleLearningController controller."""

import sys
import os 
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path + "\\lib")
from controller import Supervisor,Robot
from PyCTRNN import CTRNN
import numpy as np

# set up
robot = Supervisor()
robotBody = robot.getSelf()
goal = robot.getFromDef("goal")
timestep = int(robot.getBasicTimeStep())

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

brain = CTRNN(4)

# Helper function to set neuron led colors. Should add this to lib.
def getLedColor(value,range):
    return int(('%02x%02x%02x' % ((int(max(0,min(-1*value,range))*255/range), int(max(0,min(value,range))*255/range),0))),16)

learnIterTime = 10000
learnTimer = 0
oldDist =  np.linalg.norm(np.array(goal.getPosition())-np.array(robotBody.getPosition()))
while robot.step(timestep) != -1:

    learnTimer+=timestep
    if(learnTimer>learnIterTime):
        newDist = np.linalg.norm(np.array(goal.getPosition())-np.array(robotBody.getPosition()))
        improvement = oldDist - newDist
        brain.adapt(improvement)
        oldDist = newDist
        learnTimer=0

    brainInput = np.array([leftTouchSensor.getValue(),rightTouchSensor.getValue(),0,0])
    brainOutput = brain.step(brainInput)

    leftMotorLed.set(getLedColor(brainOutput[2],1))
    rightMotorLed.set(getLedColor(brainOutput[3],1))

    leftMotor.setVelocity(max(min(10,100*brainOutput[2]),-10))
    rightMotor.setVelocity(max(min(10,100*brainOutput[3]),-10))
    
    




