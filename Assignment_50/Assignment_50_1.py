import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class BreastCancerPrediction:
    def __init__(self):
        self.data = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()
        self.model = LogisticRegression(random_state=42)
        self.y_pred = None

    def load_data(self):
        """1. Load and explore the dataset."""
        cancer = load_breast_cancer()
        self.X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
        self.y = cancer.target
        print("Dataset loaded successfully with records:", self.X.shape)
        return self.X, self.y

    def preprocess_data(self):
        """2. Perform data preprocessing (missing values check and scaling)."""
        # Handle missing values if any
        if self.X.isnull().sum().sum() > 0:
            self.X = self.X.fillna(self.X.mean())
            
        # Normalize or scale features
        X_scaled = self.scaler.fit_transform(self.X)
        self.X = pd.DataFrame(X_scaled, columns=self.X.columns)
        print("Data preprocessing and feature scaling completed.")

    def explore_data(self):
        """3. Perform exploratory data analysis (EDA): Summary stats."""
        print("\n--- Summary Statistics ---")
        print(self.X.describe().T[['mean', 'std', 'min', 'max']].head())

    def split_data(self):
        """4. Split the dataset into training and testing sets."""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        print(f"\nTraining set shape: {self.X_train.shape}")
        print(f"Testing set shape: {self.X_test.shape}")

    def build_model(self):
        """5. Build a machine learning classification model to predict tumor type."""
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        print("\nModel training completed using Logistic Regression.")

    def evaluate_model(self):
        """6. Evaluate the model using Accuracy, Confusion Matrix, and Classification Report."""
        acc = accuracy_score(self.y_test, self.y_pred)
        cm = confusion_matrix(self.y_test, self.y_pred)
        report = classification_report(self.y_test, self.y_pred)
        
        print("\n--- Model Evaluation ---")
        print(f"Accuracy: {acc:.4f}")
        print("Confusion Matrix:\n", cm)
        print("Classification Report:\n", report)

    def conclusions(self):
        """7. Provide observations and conclusions."""
        print("\n--- Observations and Conclusions ---")
        print("- The model successfully classifies benign and malignant tumors with high accuracy.")
        print("- Feature scaling ensured that features with larger variance did not dominate the optimization process.")


def main():
    # Instantiate the class and execute steps sequentially matching deliverables
    predictor = BreastCancerPrediction()
    
    # Data loading
    predictor.load_data()
    
    # Preprocessing
    predictor.preprocess_data()
    
    # Exploratory Data Analysis
    predictor.explore_data()
    
    # Splitting dataset
    predictor.split_data()
    
    # Model building
    predictor.build_model()
    
    # Evaluation
    predictor.evaluate_model()
    
    # Conclusions
    predictor.conclusions()


if __name__ == "__main__":
    main()