from audioop import bias
import numpy

class CTRNN:


    def __init__(self, size,weightRange=4,biasRange=2):
        self.size = size
        self.potentials = numpy.zeros(size)
        self.weights = (numpy.random.rand(size,size)-0.5)*0.01
        self.bias = (numpy.random.rand(size)-0.5)*0.01
        self.timescale = numpy.full(size,0.5)
        self.weightRange = weightRange
        self.biasRange = biasRange
        self.savedWeights = numpy.zeros((size,size))
        self.savedBias = numpy.zeros(size)
        self.savedTimescale = numpy.full(size,0.5)
        numpy.copyto(self.savedWeights,self.weights)
        numpy.copyto(self.savedBias,self.bias)
        self.weights += ((numpy.random.rand(size)-0.5)*0.01).clip(-1*weightRange,weightRange)
        self.bias += ((numpy.random.rand(size)-0.5)*0.01).clip(-1*biasRange,biasRange)
        self.timescale +=((numpy.random.rand(size)-0.5)*0.01).clip(0,1)
        


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
        return (1/(1+numpy.exp(-inputVector.clip(min=100))))


    def adapt(self,improvement,improvementThreshold=0.001,mutationSize=0.001):
        if(improvement>improvementThreshold):
            numpy.copyto(self.savedWeights,self.weights)
            numpy.copyto(self.savedBias,self.bias)
            numpy.copyto(self.savedTimescale,self.timescale)
            self.weights += ((numpy.random.rand(self.size,self.size)-0.5)*mutationSize).clip(-1*self.weightRange,self.weightRange)
            self.bias += ((numpy.random.rand(self.size)-0.5)*mutationSize).clip(-1*self.biasRange,self.biasRange)
            self.timescale += ((numpy.random.rand(self.size)-0.5)*mutationSize).clip(0,1)
        else:
            self.weights = self.savedWeights + ((numpy.random.rand(self.size,self.size)-0.5)*mutationSize).clip(-1*self.weightRange,self.weightRange)
            self.bias = self.savedBias + ((numpy.random.rand(self.size)-0.5)*mutationSize).clip(-1*self.biasRange,self.biasRange)
            self.timescale = self.savedTimescale + ((numpy.random.rand(self.size)-0.5)*mutationSize).clip(0,1)







    # def adapt(self,feedback,weightMut=3,biasMut=3,timeMut=0):
    #     feedback = max(0,min(feedback,1))
    #     #where to go
    #     self.weightsTrajectory = self.weightsTrajectory*feedback + (1-feedback)*weightMut*(numpy.random.rand(self.size,self.size)-0.5)
    #     self.biasTrajectory = self.biasTrajectory*feedback + (1-feedback)*biasMut*(numpy.random.rand(self.size)-0.5)
    #     self.timescaleTrajectory = self.timescaleTrajectory*feedback + (1-feedback)*timeMut*(numpy.random.rand(self.size)-0.5)
    #     #how quick to go there
    #     self.weights += self.weightsTrajectory*self.weightLearnRate
    #     self.bias += self.biasTrajectory*self.biasLearnRate
    #     self.timescale += self.timescaleTrajectory*self.timescaleLearnRate
    #     # print(self.weightsTrajectory)
    #     # print(self.weights)
    #     # print(self.biasTrajectory)
    #     # print(self.bias)
    #     # print(self.timescale)

