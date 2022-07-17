from cgi import test

import numpy
import PyCTRNN
import numpy
import CTRNNVisualizer


brain = PyCTRNN.CTRNN(4)

brain.weights = numpy.zeros((brain.size,brain.size))
brain.bias = numpy.zeros(brain.size)

brain.weights[2,0] = 1
brain.weights[3,1] = 1
print(brain.weights)

# for i in range(10):

#     sensorInput = numpy.array([0,0,0,0])

#     brainOutput = brain.step(sensorInput)
#     print(brainOutput)


sensorInput = numpy.array([0,0,0,0])

brainOutput = brain.step(sensorInput)
print(brainOutput)