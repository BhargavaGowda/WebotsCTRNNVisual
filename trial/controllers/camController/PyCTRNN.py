import numpy

class CTRNN:


    def __init__(self, size):
        self.size = size
        self.potentials = numpy.zeros(size)
        self.weights = numpy.random.rand(size,size)-0.5
        self.bias = numpy.random.rand(size)-0.5
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

    def mutate(self,magnitude):
        self.weights += magnitude*(numpy.random.rand(self.size,self.size)-0.5)
        self.bias += magnitude*(numpy.random.rand(self.size)-0.5)
