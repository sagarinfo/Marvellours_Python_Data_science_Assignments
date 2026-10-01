import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

class CustomerChurnNN:
    def __init__(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)
        self.scaler = StandardScaler()
        # Feedforward Neural Network (Multi-Layer Perceptron)
        self.model = MLPClassifier(
            hidden_layer_sizes=(16, 8), 
            activation='relu', 
            solver='adam', 
            max_iter=1000, 
            random_state=42
        )
        self.label_map = {0: "Customer will stay", 1: "Customer will leave"}

    def preprocess(self):
        """Applies StandardScaler to scale numerical features."""
        self.X_scaled = self.scaler.fit_transform(self.X)

    def train(self):
        """Trains the FNN model on scaled training data."""
        self.model.fit(self.X_scaled, self.y)

    def evaluate(self):
        """Evaluates and prints training accuracy score."""
        predictions = self.model.predict(self.X_scaled)
        acc = accuracy_score(self.y, predictions)
        print(f"Model Accuracy: {acc * 100:.2f}%")

    def predict(self, new_customer_data):
        """Preprocesses new input data and predicts customer churn."""
        scaled_input = self.scaler.transform(new_customer_data)
        prediction_code = self.model.predict(scaled_input)[0]
        return self.label_map[prediction_code]


# Dataset setup
X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
]

y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

# Execution pipeline
churn_model = CustomerChurnNN(X, y)
churn_model.preprocess()
churn_model.train()
churn_model.evaluate()

# Test Input prediction
new_customer = [[46, 1450, 5, 6, 9]]
prediction = churn_model.predict(new_customer)
print(f"Prediction: {prediction}")