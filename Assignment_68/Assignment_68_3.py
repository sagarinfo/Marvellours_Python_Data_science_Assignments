import numpy as np

class FlattenAndDense:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def flatten(self):
        """Converts 2D feature matrix into 1D array."""
        return self.matrix.flatten()

    def forward_dense(self, vector, weights, bias):
        """Passes 1D vector into Fully Connected layer: Output = dot(x, w) + b"""
        return np.dot(vector, weights) + bias


# 2D Input Feature Matrix
matrix = [
    [6, 4],
    [8, 6]
]

processor = FlattenAndDense(matrix)

# 1. Flatten
flattened_vector = processor.flatten()
print("1D Flattened Vector:")
print(flattened_vector)

# 2. Dense Layer Execution
# Assume predefined weights for 4 inputs to 1 output neuron, and 1 bias term
weights = np.array([0.5, -0.2, 0.1, 0.3])
bias = 0.5

dense_output = processor.forward_dense(flattened_vector, weights, bias)

print("\n--- Manual Dense Calculation ---")
print(f"Inputs (X)  : {flattened_vector}")
print(f"Weights (W) : {weights}")
print(f"Bias (b)    : {bias}")
print(f"Calculated Final Output: {dense_output:.2f}")