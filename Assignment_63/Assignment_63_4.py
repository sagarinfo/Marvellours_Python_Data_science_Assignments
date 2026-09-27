import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

class LearningRateExperiment:
    def __init__(self, filepath='Loan_Default.csv'):
        self.filepath = filepath
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        self.numerical_cols = []
        self.categorical_cols = []
        self._prepare_data()

    def _prepare_data(self):
        try:
            df = pd.read_csv(self.filepath)
        except FileNotFoundError:
            np.random.seed(42)
            n = 500
            df = pd.DataFrame({
                'Age': np.random.randint(21, 70, n),
                'Income': np.random.randint(30000, 150000, n),
                'LoanAmount': np.random.randint(5000, 50000, n),
                'CreditScore': np.random.randint(550, 850, n),
                'EmploymentYears': np.random.randint(0, 30, n),
                'ExistingLoans': np.random.randint(0, 5, n),
                'MonthlyDebt': np.random.randint(200, 3000, n),
                'LoanTerm': np.random.choice([12, 36, 60], n),
                'PreviousDefault': np.random.choice(['Yes', 'No'], n, p=[0.2, 0.8]),
                'HomeOwnership': np.random.choice(['Rent', 'Own', 'Mortgage'], n),
                'Default': np.random.choice([0, 1], n, p=[0.7, 0.3])
            })

        X = df.drop(columns=['Default'])
        y = df['Default']
        self.numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
        self.categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

    def run_experiment(self):
        learning_rates = [0.0001, 0.001, 0.01, 0.1]
        results = {}

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numerical_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_cols)
            ]
        )

        print("--- Running Experiment 3: Learning Rate (learning_rate_init) ---")
        for lr in learning_rates:
            pipeline = Pipeline(steps=[
                ('preprocessor', preprocessor),
                ('classifier', MLPClassifier(
                    hidden_layer_sizes=(32, 16),
                    activation='relu',
                    solver='adam',
                    learning_rate_init=lr,
                    max_iter=1000,
                    random_state=42
                ))
            ])
            pipeline.fit(self.X_train, self.y_train)
            y_pred = pipeline.predict(self.X_test)
            acc = accuracy_score(self.y_test, y_pred)
            results[lr] = acc
            print(f"Learning Rate: {lr} -> Accuracy: {acc:.4f}")

        return results

def main():
    experiment = LearningRateExperiment()
    experiment.run_experiment()

if __name__ == '__main__':
    main()