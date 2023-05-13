import numpy as np

def sigmoid(x):
  # Наша функция активации: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
  # Производная сигмоиды: f'(x) = f(x) * (1 - f(x))
  fx = sigmoid(x)
  return fx * (1 - fx)

def mse_loss(y_true, y_pred):
  # y_true и y_pred - массивы numpy одинаковой длины.
  return ((y_true - y_pred) ** 2).mean()

class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias
  def feedforward(self, inputs):
    total = np.dot(self.weights, inputs) + self.bias
    return sigmoid(total)

  def deriv(self, inputs):
    total = np.dot(self.weights, inputs) + self.bias
    return deriv_sigmoid(total)

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
  def __init__(self, amountInputs, amountLayer, amountNeuron):
    self.amountInputs = amountInputs
    self.amountLayer = amountLayer
    self.amountNeuron = amountNeuron
    self.networkLayer = list()
    self.amountNeuron.insert(0, amountInputs)
    for i in range(amountLayer):
      self.networkLayer.append(neuronRNDGenerator(amountNeuron[i+1], amountNeuron[i]))
    self.networkOutput = outputNeuron(amountNeuron[amountLayer])
    self.networkLayer.append([self.networkOutput, ])
  def feedforward(self, inputs):
    self.inputs_for_outputLayer = []
    self.inputs_for_outputLayer.insert(0, inputs)
    for i in range(self.amountLayer):
      inputs_for_outputNeuron = []
      for j in range(self.amountNeuron[i+1]):
        inputs_for_outputNeuron.append(self.networkLayer[i][j].feedforward(self.inputs_for_outputLayer[i]))
      self.inputs_for_outputLayer.append(inputs_for_outputNeuron)
    self.resultNN = self.networkOutput.feedforward(self.inputs_for_outputLayer[self.amountLayer])
    return self.resultNN

  def train(self, x_data, y_data):
    learn_rate = 0.1
    epochs = 1000

    for epoch in range(epochs):
      for x, y_true in zip(x_data, y_data):
        # --- Прямой проход (эти значения нам понадобятся позже)
        y_pred = self.feedforward(x)
        e = y_pred - y_true
        self.delta_layer = []

        for i in reversed(range(len(self.networkLayer))):
          delta_neuron = []
          if i == len(self.networkLayer) - 1:
            this_delta = e * deriv_sigmoid(y_pred)
            for _ in range(len(self.networkOutput.weights)):
              delta_neuron.append(this_delta)
          else:
            for j in range(len(self.networkLayer[i])):
              this_delta = 0
              for k in range(len(self.networkLayer[i+1])):
                this_delta += self.networkLayer[i+1][k].weights[j] * self.delta_layer[len(self.networkLayer) - i - 2][k]
              delta_neuron.append(this_delta * deriv_sigmoid(self.inputs_for_outputLayer[i+1][j]))
          self.delta_layer.append(delta_neuron)

        for i in range(len(self.networkLayer)):
          for j in range(len(self.networkLayer[i])):
            for k in range(len(self.networkLayer[i][j].weights)):
                self.networkLayer[i][j].weights[k] += -learn_rate * self.delta_layer[len(self.networkLayer) - i - 1][j] * self.inputs_for_outputLayer[i][k]

        if epoch % 10 == 0:
          y_pred = np.apply_along_axis(self.feedforward, 1, x_data)
          loss = mse_loss(y_data, y_pred)
          print("Epoch %d loss: %.3f" % (epoch, loss))

test_nn_1 = oneNeuralNetwork(3, 1, [2])

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
