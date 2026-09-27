import numpy as np
import matplotlib.pyplot as plt

class ActivationVisualizer:
    def __init__(self, start=-10, stop=10, num=400):
        self.x = np.linspace(start, stop, num)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def tanh(self, x):
        return np.tanh(x)

    def plot_all(self):
        y_sigmoid = self.sigmoid(self.x)
        y_relu = self.relu(self.x)
        y_tanh = self.tanh(self.x)

        plt.figure(figsize=(10, 6))
        plt.plot(self.x, y_sigmoid, label="Sigmoid", linewidth=2)
        plt.plot(self.x, y_relu, label="ReLU", linewidth=2)
        plt.plot(self.x, y_tanh, label="Tanh", linewidth=2)

        plt.title("Activation Functions (-10 to 10)")
        plt.xlabel("Input Value (x)")
        plt.ylabel("Output Value")
        plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
        plt.axvline(0, color='black', linestyle='--', linewidth=0.7)
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend(fontsize=12)
        plt.ylim(-1.5, 2.0)
        plt.show()

# Instantiate and plot
visualizer = ActivationVisualizer()
visualizer.plot_all()