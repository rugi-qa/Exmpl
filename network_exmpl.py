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

x_data = np.array([
  [5, 3, 2],  #  Axe
  [2, 2, 6],  #  Keeper
  [1, 5, 4],  #  Drow
  [2, 5, 3],  #  Slark
  [4, 2, 4],  #  Shaker
  [6, 2, 2],  #  Pudge
  [2, 4, 4],  #  Fiend
  [2, 3, 5],  #  Dazzle
  [5, 2, 3]   #  Mars
])
y_data = np.array([
  0,  #  Tank
  0.5,  #  Support
  1,  #  Carry
  1,
  0.5,
  0,
  1,
  0.5,
  0
])
