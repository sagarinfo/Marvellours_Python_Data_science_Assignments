import numpy as np

class ArtificialNeuron:
    def __init__(self, weights, bias):
        self.weights = np.array(weights)
        self.bias = bias

    def calculate_weighted_sum(self, inputs):
        """Calculates z = sum(w_i * x_i) + bias"""
        inputs = np.array(inputs)
        return np.dot(self.weights, inputs) + self.bias

    def sigmoid(self, z):
        """Applies Sigmoid Activation: 1 / (1 + e^(-z))"""
        return 1 / (1 + np.exp(-z))

    def forward(self, inputs):
        z = self.calculate_weighted_sum(inputs)
        output = self.sigmoid(z)
        return z, output


# Given inputs
x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

# Instantiate and execute
neuron = ArtificialNeuron(weights=[w1, w2], bias=bias)
weighted_sum, final_output = neuron.forward([x1, x2])

print(f"Weighted Sum (z): {weighted_sum:.4f}")
print(f"Final Output: {final_output:.4f}")