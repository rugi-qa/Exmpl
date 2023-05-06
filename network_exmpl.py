import numpy as np

def sigmoid(x):
  # Наша функция активации: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

def neuronRNDGenerator(amountNeuron, amountInputs):
    neuronsList = []
    for _ in range(amountNeuron):
        weights = []
        for _ in range(amountInputs):
            weights.append(np.random.normal())
        bias = np.random.normal()
        neuronsList.append(Neuron(weights, bias))
    return neuronsList

def outputNeuron(amountInputs):
    weights = []
    for _ in range(amountInputs):
        weights.append(np.random.normal())
    bias = np.random.normal()
    outNeuron = Neuron(weights, bias)
    return outNeuron

class oneNeuralNetwork:
    def __init__(self, amountNeuron, amountInputs):
        self.amountNeuron = amountNeuron
        self.amountInputs = amountInputs
        self.networkNeurons = neuronRNDGenerator(amountNeuron, amountInputs)
        self.networkOutput = outputNeuron(amountNeuron)
    
    def feedforward(self, inputs):
        self.inputs_for_outputNeuron = []
        for i in range(self.amountNeuron):            
            self.inputs_for_outputNeuron.append(self.networkNeurons[i].feedforward(inputs))
        self.resultNN = self.networkOutput.feedforward(self.inputs_for_outputNeuron)
        return self.resultNN

test_nn_1 = oneNeuralNetwork(3,2)
print(test_nn_1.networkNeurons[1].weights)
print(test_nn_1.feedforward([1, 2]))
