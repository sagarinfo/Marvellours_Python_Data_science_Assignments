import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_recall_fscore_support

class LoanDefaultPredictor:
    def __init__(self, filepath='Loan_Default.csv'):
        self.filepath = filepath
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.pipeline = None
        self.model = None

    def load_data(self):
        """Task 1 & 3: Load dataset and check missing values."""
        print("--- Task 1: Loading Dataset ---")
        try:
            self.df = pd.read_csv(self.filepath)
        except FileNotFoundError:
            print(f"File {self.filepath} not found. Creating a synthetic mock dataframe for demonstration.")
            np.random.seed(42)
            n = 500
            self.df = pd.DataFrame({
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
            
        print("\n--- Task 3: Missing Values ---")
        print(self.df.isnull().sum())

    def exploratory_analysis(self):
        """Task 2 & 4: Exploratory analysis and class balance check."""
        print("\n--- Task 2: Exploratory Analysis ---")
        print(self.df.info())
        print(self.df.describe())
        
        print("\n--- Task 4: Target Class Balance ---")
        print(self.df['Default'].value_counts())
        print(f"Proportion:\n{self.df['Default'].value_counts(normalize=True)}")

    def preprocess_and_split(self):
        """Task 5, 6, 7, 8 & 9: Encoding, Separation, Splitting, Stratification explanation, Scaling."""
        print("\n--- Task 5 & 6: Separate X and y & Encoding Categorical Variables ---")
        X = self.df.drop(columns=['Default'])
        y = self.df['Default']

        categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
        numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

        print(f"Categorical features: {categorical_cols}")
        print(f"Numerical features: {numerical_cols}")

        print("\n--- Task 7 & 8: Splitting Dataset and Stratification Explanation ---")
        print("Task 8 Explanation: Stratified splitting is essential because loan default datasets are typically imbalanced. Stratification ensures that train and test sets preserve the identical percentage of target classes as the source dataset.")

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        print("\n--- Task 9: Feature Scaling & Pipeline Setup ---")
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
            ]
        )

        # Task 10: MLP Classifier specification
        self.model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation='relu',
            solver='adam',
            max_iter=1000,
            random_state=42
        )

        self.pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', self.model)
        ])

    def train_model(self):
        """Task 11 & 16: Train model and plot loss."""
        print("\n--- Task 11: Training the Model ---")
        self.pipeline.fit(self.X_train, self.y_train)
        print("Training completed.")

        print("\n--- Task 16: Plotting Training Loss ---")
        mlp_classifier = self.pipeline.named_steps['classifier']
        plt.figure(figsize=(8, 5))
        plt.plot(mlp_classifier.loss_curve_, marker='o', color='purple')
        plt.title('MLP Training Loss Curve')
        plt.xlabel('Iterations (Epochs)')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.show()

    def evaluate_model(self):
        """Task 12, 13, 14, 15: Accuracy, Confusion Matrix, Classification Report, Precision/Recall/F1."""
        print("\n--- Evaluation Phase ---")
        y_pred = self.pipeline.predict(self.X_test)

        print(f"\n--- Task 12: Accuracy ---")
        acc = accuracy_score(self.y_test, y_pred)
        print(f"Accuracy: {acc:.4f}")

        print(f"\n--- Task 13: Confusion Matrix ---")
        print(confusion_matrix(self.y_test, y_pred))

        print(f"\n--- Task 14: Classification Report ---")
        print(classification_report(self.y_test, y_pred))

        print(f"\n--- Task 15: Precision, Recall, and F1-Score ---")
        precision, recall, f1, _ = precision_recall_fscore_support(self.y_test, y_pred, average='binary')
        print(f"Precision: {precision:.4f} | Recall: {recall:.4f} | F1-Score: {f1:.4f}")

    def test_new_applicants(self):
        """Task 17: Test the model on new loan applicants."""
        print("\n--- Task 17: Testing on New Loan Applicants ---")
        new_applicants = pd.DataFrame({
            'Age': [35, 50, 24],
            'Income': [60000, 120000, 32000],
            'LoanAmount': [15000, 30000, 10000],
            'CreditScore': [720, 810, 590],
            'EmploymentYears': [5, 15, 1],
            'ExistingLoans': [1, 0, 2],
            'MonthlyDebt': [500, 800, 900],
            'LoanTerm': [36, 60, 12],
            'PreviousDefault': ['No', 'No', 'Yes'],
            'HomeOwnership': ['Own', 'Mortgage', 'Rent']
        })

        predictions = self.pipeline.predict(new_applicants)
        for i, pred in enumerate(predictions):
            status = "1 -> High default risk" if pred == 1 else "0 -> Low default risk"
            print(f"Applicant {i+1} Prediction: {status}")

def main():
    predictor = LoanDefaultPredictor()
    predictor.load_data()
    predictor.exploratory_analysis()
    predictor.preprocess_and_split()
    predictor.train_model()
    predictor.evaluate_model()
    predictor.test_new_applicants()

if __name__ == '__main__':
    main()