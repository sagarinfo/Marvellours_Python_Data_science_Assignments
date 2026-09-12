import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

class LoanApprovalVotingClassifier:
    def __init__(self, df):
        """Initializes the class with the loan dataset."""
        self.df = df
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
        self.lr_model = LogisticRegression(random_state=42)
        self.dt_model = DecisionTreeClassifier(random_state=42)
        self.knn_model = KNeighborsClassifier()
        
        self.hard_voting_model = None
        self.soft_voting_model = None
        
        self.accuracies = {}

    def check_missing_values(self):
        """Task 2: Check for missing values."""
        missing = self.df.isnull().sum()
        print("Task 2 - Missing Values Check:\n", missing)
        # Handle missing values if any exist by filling with median/mean
        if missing.sum() > 0:
            self.df = self.df.fillna(self.df.median(numeric_only=True))

    def separate_variables(self, target_column):
        """Task 3: Separate input and output variables."""
        self.X = self.df.drop(columns=[target_column])
        self.y = self.df[target_column]
        print("Task 3 - Input and output variables separated successfully.")

    def split_data(self):
        """Task 4: Split the dataset into training and testing data."""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        print("Task 4 - Dataset split into training and testing sets.")

    def train_individual_models(self):
        """Tasks 5, 6, 7 & 8: Train Logistic Regression, Decision Tree, KNN and calculate individual accuracies."""
        # Task 5: Train Logistic Regression
        self.lr_model.fit(self.X_train, self.y_train)
        lr_pred = self.lr_model.predict(self.X_test)
        lr_acc = accuracy_score(self.y_test, lr_pred)
        self.accuracies['Logistic Regression'] = lr_acc

        # Task 6: Train Decision Tree
        self.dt_model.fit(self.X_train, self.y_train)
        dt_pred = self.dt_model.predict(self.X_test)
        dt_acc = accuracy_score(self.y_test, dt_pred)
        self.accuracies['Decision Tree'] = dt_acc

        # Task 7: Train KNN
        self.knn_model.fit(self.X_train, self.y_train)
        knn_pred = self.knn_model.predict(self.X_test)
        knn_acc = accuracy_score(self.y_test, knn_pred)
        self.accuracies['KNN'] = knn_acc

        print("Tasks 5-8 - Individual models trained and individual accuracies calculated.")

    def evaluate_voting_classifiers(self):
        """Tasks 9, 10, 11, 12 & 13: Create and evaluate Hard and Soft Voting Classifiers."""
        estimators = [
            ('lr', self.lr_model),
            ('dt', self.dt_model),
            ('knn', self.knn_model)
        ]

        # Task 9 & 10: Hard Voting Classifier & Accuracy
        self.hard_voting_model = VotingClassifier(estimators=estimators, voting='hard')
        self.hard_voting_model.fit(self.X_train, self.y_train)
        hard_pred = self.hard_voting_model.predict(self.X_test)
        hard_acc = accuracy_score(self.y_test, hard_pred)
        self.accuracies['Hard Voting'] = hard_acc

        # Task 11 & 12: Soft Voting Classifier & Accuracy
        self.soft_voting_model = VotingClassifier(estimators=estimators, voting='soft')
        self.soft_voting_model.fit(self.X_train, self.y_train)
        soft_pred = self.soft_voting_model.predict(self.X_test)
        soft_acc = accuracy_score(self.y_test, soft_pred)
        self.accuracies['Soft Voting'] = soft_acc

        print("Tasks 9-12 - Voting classifiers evaluated.")

    def display_comparison_table(self):
        """Task 13: Compare results in a tabular format matching assignment layout."""
        print("\n--- Model Performance Comparison ---")
        comparison_df = pd.DataFrame(list(self.accuracies.items()), columns=['Model', 'Accuracy'])
        print(comparison_df.to_string(index=False))


def main():
    # Task 1: Load the dataset (using synthetic sample data matching the attributes for execution illustration)
    np.random.seed(42)
    n_samples = 300
    data = {
        'Age': np.random.randint(21, 65, size=n_samples),
        'Income': np.random.randint(25000, 120000, size=n_samples),
        'CreditScore': np.random.randint(550, 850, size=n_samples),
        'ExistingLoan': np.random.randint(0, 2, size=n_samples),
        'EmploymentExperience': np.random.randint(0, 30, size=n_samples),
        'LoanAmount': np.random.randint(10000, 500000, size=n_samples),
        'LoanApproved': np.random.randint(0, 2, size=n_samples) # Target Column: 0 -> Rejected, 1 -> Approved
    }
    df = pd.DataFrame(data)
    print("Task 1 - Dataset loaded successfully.")

    # Initialize the workflow class
    pipeline = LoanApprovalVotingClassifier(df)

    # Execute workflow steps sequentially
    pipeline.check_missing_values()
    pipeline.separate_variables(target_column='LoanApproved')
    pipeline.split_data()
    pipeline.train_individual_models()
    pipeline.evaluate_voting_classifiers()
    pipeline.display_comparison_table()

if __name__ == "__main__":
    main()