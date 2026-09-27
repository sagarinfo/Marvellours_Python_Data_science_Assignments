class WeightUpdater:
    def __init__(self, x, weight, bias, target, learning_rate):
        self.x = x
        self.weight = weight
        self.bias = bias
        self.target = target
        self.lr = learning_rate

    def predict(self):
        """Linear prediction: y_pred = w * x + b"""
        return (self.weight * self.x) + self.bias

    def calculate_error(self, y_pred):
        """Error = y_pred - y_target"""
        return y_pred - self.target

    def update_weights(self):
        y_pred = self.predict()
        error = self.calculate_error(y_pred)

        # Gradient of MSE loss w.r.t weight: dL/dw = error * x
        dw = error * self.x
        db = error

        old_weight = self.weight
        old_bias = self.bias

        # Weight update rule: w_new = w_old - (learning_rate * gradient)
        self.weight = self.weight - (self.lr * dw)
        self.bias = self.bias - (self.lr * db)

        return old_weight, self.weight, y_pred, error


# Initial parameter configuration
updater = WeightUpdater(x=2.0, weight=0.8, bias=0.1, target=1.0, learning_rate=0.1)

old_w, new_w, prediction, error = updater.update_weights()

print(f"Initial Prediction: {prediction:.4f}")
print(f"Calculated Error:   {error:.4f}")
print(f"Old Weight:        {old_w:.4f}")
print(f"Updated Weight:    {new_w:.4f}")