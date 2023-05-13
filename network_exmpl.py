import numpy as np

def sigmoid(x):
  # Наша функция активации: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def div(x):
    return sigmoid(x)*(1 - sigmoid(x))

def qual(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


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

    def train(self, x_data, y_data):
        epochs = 1000
        step = 0.01
        for epoch in range(epochs):
            for x, y_true in zip(x_data, y_data):
                y_pred = self.feedforward(x)               
                e = y_pred - y_true
                delta = e * div(y_pred)
                for i in range(len(self.networkOutput.weights)):
                        self.networkOutput.weights[i] = self.networkOutput.weights[i] - step * delta * self.inputs_for_outputNeuron[i]
                self.deltaNeuron = []

                for i in range(self.amountNeuron):
                        self.deltaNeuron.append(delta*self.networkOutput.weights[i]*div(self.inputs_for_outputNeuron[i]))
                        for j in range(len(self.networkNeurons[i].weights)):
                            self.networkNeurons[i].weights[j] = self.networkNeurons[i].weights[j] - step * self.deltaNeuron[i] * x[j]

                if epoch % 10 == 0:
                        y_pred = np.apply_along_axis(self.feedforward, 1, x_data)
                        loss = qual(y_data, y_pred)
                        print("Epoch %d loss: %.3f" % (epoch, loss))

test_nn_1 = oneNeuralNetwork(2,3)

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

test_nn_1.train(x_data, y_data)

fura = np.array([2, 3, 5])

print("Фурион: %.3f" % test_nn_1.feedforward(fura))
