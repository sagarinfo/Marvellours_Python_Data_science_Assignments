import numpy as np

class CNNOperations:
    def __init__(self, feature_map):
        self.feature_map = np.array(feature_map)

    def apply_relu(self):
        """ReLU Rule: converts values < 0 to 0, keeps values >= 0 unchanged."""
        return np.maximum(0, self.feature_map)

    def apply_max_pooling(self, matrix, pool_size=(2, 2), stride=1):
        """Extracts maximum value within pooling windows."""
        h, w = matrix.shape
        p_h, p_w = pool_size
        
        out_h = (h - p_h) // stride + 1
        out_w = (w - p_w) // stride + 1
        pooled_output = np.zeros((out_h, out_w), dtype=int)

        for i in range(out_h):
            for j in range(out_w):
                window = matrix[i*stride : i*stride + p_h, j*stride : j*stride + p_w]
                pooled_output[i, j] = np.max(window)

        return pooled_output


# Input Feature Map
feature_map = [
    [ 3,  3,  3],
    [ 0,  0,  0],
    [-3, -3, -3]
]

cnn_ops = CNNOperations(feature_map)

# Step 1: Apply ReLU
relu_output = cnn_ops.apply_relu()
print("1. Output after ReLU:")
print(relu_output)

# Step 2: Apply Max Pooling (2x2)
pooled_output = cnn_ops.apply_max_pooling(relu_output, pool_size=(2, 2), stride=1)
print("\n2. Output after 2x2 Max Pooling:")
print(pooled_output)