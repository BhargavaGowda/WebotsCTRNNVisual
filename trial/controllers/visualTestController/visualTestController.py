"""visualTestController controller."""


from cmath import inf
from time import time


from controller import Robot
import sys
import os 
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path + "\\lib")
from PyCTRNN import CTRNN
import numpy as np

def getLedColor(value,range):
    return int(('%02x%02x%02x' % ((int(max(0,min(-1*value,range))*255/range), int(max(0,min(value,range))*255/range),0))),16)

robot = Robot()
timestep = int(robot.getBasicTimeStep())

ds1 = robot.getDevice("distance sensor 1")
ds2 = robot.getDevice("distance sensor 2")
ds1.enable(timestep)
ds2.enable(timestep)
nr1 = robot.getDevice("neuron 1")
nr2 = robot.getDevice("neuron 2")
nr3 = robot.getDevice("neuron 3")
nr4 = robot.getDevice("neuron 4")

headMotor = robot.getDevice("headMotor")
headMotor.setPosition(float(inf))

brain = CTRNN(4)

brain.weights = np.array([[0.09676043,  0.10304022,  0.28637696, -0.30732528],[-0.32507208,  0.16624745, -0.02710929, -0.16294889],[-0.28085107, -0.07937742,  0.07761356,  0.48819756],[ 0.11459461, -0.41337563, -0.06034716,  0.27877888]])
brain.bias = np.array([-0.18720054, -0.30152419,  0.38290068, -0.07629804])
brain.timescale = np.array([0.5,0.5,0.5,0.5])
print(brain.weights)
print(brain.bias)





while robot.step(timestep) != -1:

    brainInput = np.array([ds1.getValue(),ds2.getValue(),0,0])
    brainOutput = brain.step(brainInput)
    nr1.set(getLedColor(brainOutput[0],4))
    nr2.set(getLedColor(brainOutput[1],4))
    nr3.set(getLedColor(brainOutput[2],4))
    nr4.set(getLedColor(brainOutput[3],4))
    headMotor.setVelocity(brainOutput[3]*4)

# Enter here exit cleanup code.

