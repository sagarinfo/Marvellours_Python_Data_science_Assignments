import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

class LoanApprovalNN:
    def __init__(self, X, y):
        self.X = np.array(X, dtype=float)
        self.y = np.array(y)
        self.scaler = StandardScaler()
        # Feedforward Neural Network Classifier
        self.model = MLPClassifier(
            hidden_layer_sizes=(16, 8), 
            activation='relu', 
            solver='adam', 
            max_iter=1000, 
            random_state=42
        )
        self.status_map = {0: "Loan Rejected", 1: "Loan Approved"}

    def preprocess(self):
        """Applies Feature Scaling to training inputs."""
        self.X_scaled = self.scaler.fit_transform(self.X)

    def train(self):
        """Trains the FNN classifier on feature vectors."""
        self.model.fit(self.X_scaled, self.y)

    def evaluate(self):
        """Evaluates model performance accuracy."""
        predictions = self.model.predict(self.X_scaled)
        acc = accuracy_score(self.y, predictions)
        print(f"Model Accuracy: {acc * 100:.2f}%")

    def predict(self, applicant_data):
        """Scales new applicant vector and predicts approval result."""
        scaled_applicant = self.scaler.transform(applicant_data)
        prediction_code = self.model.predict(scaled_applicant)[0]
        return self.status_map[prediction_code]


# Dataset setup
X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

# Execution pipeline
loan_model = LoanApprovalNN(X, y)
loan_model.preprocess()
loan_model.train()
loan_model.evaluate()

# Test Input prediction
new_applicant = [[55000, 720, 400000, 10000, 1]]
prediction = loan_model.predict(new_applicant)
print(f"Prediction: {prediction}")