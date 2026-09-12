import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class FraudDetectionPipeline:
    def __init__(self, df):
        """Initializes the pipeline with the dataset."""
        self.df = df
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.results = []

    def preprocess_data(self, target_column):
        """Separates features and target, and splits data into training and testing sets."""
        self.X = self.df.drop(columns=[target_column])
        self.y = self.df[target_column]
        
        # Split the dataset (80% train, 20% test)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        print("Data preprocessing and splitting completed.")

    def evaluate_model(self, name, model):
        """Trains a model and evaluates its performance metrics."""
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        
        acc = accuracy_score(self.y_test, y_pred)
        prec = precision_score(self.y_test, y_pred, zero_division=0)
        rec = recall_score(self.y_test, y_pred, zero_division=0)
        f1 = f1_score(self.y_test, y_pred, zero_division=0)
        cm = confusion_matrix(self.y_test, y_pred)
        
        # Store results for final comparison table
        self.results.append({
            'Algorithm': name,
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'F1': f1
        })
        
        print(f"\n--- {name} Results ---")
        print(f"Accuracy:  {acc:.4f}")
        print(f"Precision: {prec:.4f}")
        print(f"Recall:    {rec:.4f}")
        print(f"F1 Score:  {f1:.4f}")
        print(f"Confusion Matrix:\n{cm}")

    def run_all_models(self):
        """Builds and evaluates all five required models."""
        # 1. Decision Tree
        dt_model = DecisionTreeClassifier(random_state=42)
        self.evaluate_model("Decision Tree", dt_model)

        # 2. Bagging Classifier
        bagging_model = BaggingClassifier(estimator=DecisionTreeClassifier(random_state=42), n_estimators=50, random_state=42)
        self.evaluate_model("Bagging", bagging_model)

        # 3. Random Forest Classifier
        rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.evaluate_model("Random Forest", rf_model)

        # 4. AdaBoost Classifier
        ada_model = AdaBoostClassifier(random_state=42)
        self.evaluate_model("AdaBoost", ada_model)

        # 5. Voting Classifier
        voting_model = VotingClassifier(
            estimators=[
                ('dt', DecisionTreeClassifier(random_state=42)),
                ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
                ('ada', AdaBoostClassifier(random_state=42))
            ],
            voting='hard'
        )
        self.evaluate_model("Voting", voting_model)

    def display_final_comparison(self):
        """Displays the final summary comparison table."""
        print("\n==============================================")
        print("         FINAL MODEL COMPARISON TABLE         ")
        print("==============================================")
        comparison_df = pd.DataFrame(self.results)
        print(comparison_df.to_string(index=False))


def main():
    # Generate a synthetic dataset mimicking the transaction details for execution
    np.random.seed(42)
    n_samples = 400
    data = {
        'TransactionAmount': np.random.uniform(10.0, 5000.0, size=n_samples),
        'TransactionTime': np.random.randint(0, 24, size=n_samples),
        'AccountAge': np.random.randint(1, 3650, size=n_samples),
        'NumberOfPreviousTransactions': np.random.randint(0, 100, size=n_samples),
        'LocationDifference': np.random.uniform(0.0, 500.0, size=n_samples),
        'DeviceType': np.random.randint(0, 3, size=n_samples),
        'FailedLoginAttempts': np.random.randint(0, 5, size=n_samples),
        'Fraud': np.random.choice([0, 1], size=n_samples, p=[0.85, 0.15]) # 0: Normal, 1: Fraudulent
    }
    
    df = pd.DataFrame(data)
    print("Dataset successfully generated/loaded.")

    # Instantiate the pipeline class
    pipeline = FraudDetectionPipeline(df)
    
    # Preprocess data (split features and target)
    pipeline.preprocess_data(target_column='Fraud')
    
    # Build, train, and evaluate all models
    pipeline.run_all_models()
    
    # Display the final comparison table
    pipeline.display_final_comparison()

if __name__ == "__main__":
    main()