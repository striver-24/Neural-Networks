import numpy as np

def sigmoid(x):
    # Our activation function : f(x)=1/(1 + e^(-x))
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        #Weight inputs, add bias, then use activation function
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
    
weights = np.array([0,1])
bias = 4
n = Neuron(weights, bias)

x = np.array([4,5])
print(n.feedforward(x))
        