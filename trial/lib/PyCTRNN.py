import numpy

class CTRNN:


    def __init__(self, size, weightRange=4,biasRange=2):
        self.size = size
        self.weightRange = weightRange
        self.biasRange = biasRange
        self.potentials = numpy.zeros(size)
        self.weights = (numpy.random.rand(size,size)-0.5)*weightRange
        self.bias = (numpy.random.rand(size)-0.5)*biasRange
        self.timescale = numpy.full(size,0.5)


    def getWeights(self):
        return self.weights

    def getBias(self):
        return self.bias

    def getTimescale(self):
        return self.timescale
    
    def getPotentials(self):
        return self.potentials

    def step(self, inputArray):
        self.potentials += self.timescale*(inputArray - self.potentials + numpy.matmul(self.weights, self.sigmoid(self.potentials+self.bias)))
        return self.potentials

    def sigmoid(self,inputVector):
        return (1/(1+numpy.exp(-inputVector)))
