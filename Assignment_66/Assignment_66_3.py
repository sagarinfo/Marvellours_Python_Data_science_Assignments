import numpy as np

class LossCalculator:
    def __init__(self, y_true, y_pred):
        self.y_true = np.array(y_true, dtype=float)
        self.y_pred = np.array(y_pred, dtype=float)

    def mean_squared_error(self):
        """MSE = (1/N) * sum((y_true - y_pred)^2)"""
        return np.mean((self.y_true - self.y_pred) ** 2)

    def binary_cross_entropy(self):
        """BCE = -1/N * sum(y*log(p) + (1-y)*log(1-p))"""
        # Epsilon prevents log(0) undefined errors
        epsilon = 1e-15
        y_pred_clipped = np.clip(self.y_pred, epsilon, 1 - epsilon)
        bce = -np.mean(
            self.y_true * np.log(y_pred_clipped) + 
            (1 - self.y_true) * np.log(1 - y_pred_clipped)
        )
        return bce


# Sample datasets
y_actual = [1.0, 0.0, 1.0, 1.0]
y_predicted = [0.9, 0.1, 0.8, 0.65]

calc = LossCalculator(y_actual, y_predicted)

print(f"Mean Squared Error (MSE): {calc.mean_squared_error():.4f}")
print(f"Binary Cross Entropy (BCE): {calc.binary_cross_entropy():.4f}")