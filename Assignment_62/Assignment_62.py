import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

class EmployeeAttritionPredictor:
    def __init__(self, filepath='Employee_Attrition.csv'):
        self.filepath = filepath
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()
        # MLP with at least two hidden layers (e.g., 16 and 8 neurons)
        self.model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=42)

    def load_and_explore_data(self):
        """Task 1, 2, 3, 4: Load dataset, display properties, check missing values, and identify features."""
        print("--- 1. Loading Dataset ---")
        self.df = pd.read_csv(self.filepath)
        
        print("\n--- 2. Shape, Columns, and First 5 Records ---")
        print(f"Dataset Shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")
        print("\nFirst 5 records:")
        print(self.df.head())
        
        print("\n--- 3. Checking for Missing Values ---")
        print(self.df.isnull().sum())
        
        print("\n--- 4. Identifying Numerical and Categorical Features ---")
        numerical_features = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_features = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        print(f"Numerical Features: {numerical_features}")
        print(f"Categorical Features: {categorical_features}")

    def preprocess_data(self):
        """Task 5, 6, 7, 8, 9: Encode categorical variables, split features/labels, train/test split, and scale."""
        print("\n--- 5 & 6. Converting Categorical & Target Variables ---")
        # Convert OverTime: Yes -> 1, No -> 0
        if 'OverTime' in self.df.columns:
            self.df['OverTime'] = self.df['OverTime'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
            
        # Convert Attrition (Target): Yes -> 1, No -> 0
        if 'Attrition' in self.df.columns:
            self.df['Attrition'] = self.df['Attrition'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

        print("\n--- 7. Separating Independent and Dependent Variables ---")
        X = self.df.drop(columns=['Attrition'])
        y = self.df['Attrition']

        print("\n--- 8. Dividing Dataset into Training and Testing Data ---")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        print("\n--- 9. Applying Feature Scaling ---")
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

    def train_network(self):
        """Task 10, 11, 12: Design MLP, train the network, and display iterations."""
        print("\n--- 10 & 11. Designing and Training the MLP Network ---")
        self.model.fit(self.X_train, self.y_train)
        
        print(f"\n--- 12. Number of Iterations Required for Training ---")
        print(f"Actual iterations (epochs): {self.model.n_iter_}")

    def evaluate_model(self):
        """Task 13, 14, 15, 16, 19: Accuracies, confusion matrix, loss curve, and performance analysis."""
        print("\n--- 13 & 14. Calculating Training and Testing Accuracy ---")
        train_pred = self.model.predict(self.X_train)
        test_pred = self.model.predict(self.X_test)
        
        train_acc = accuracy_score(self.y_train, train_pred)
        test_acc = accuracy_score(self.y_test, test_pred)
        
        print(f"Training Accuracy: {train_acc:.4f}")
        print(f"Testing Accuracy: {test_acc:.4f}")

        print("\n--- 15. Generating Confusion Matrix ---")
        cm = confusion_matrix(self.y_test, test_pred)
        print(cm)

        print("\n--- 16. Plotting the Loss Curve ---")
        plt.figure(figsize=(8, 5))
        plt.plot(self.model.loss_curve_, marker='o', color='b')
        plt.title('MLP Training Loss Curve')
        plt.xlabel('Iterations / Epochs')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.show()

        print("\n--- 19. Overfitting or Underfitting Analysis ---")
        if train_acc > 0.95 and test_acc < (train_acc - 0.10):
            print("Analysis: The model is suffering from **Overfitting** (high training accuracy, lower testing accuracy).")
        elif train_acc < 0.70 and test_acc < 0.70:
            print("Analysis: The model is suffering from **Underfitting** (low training and testing accuracy).")
        else:
            print("Analysis: The model shows a balanced performance between training and testing data with acceptable generalization.")

    def PredictAttrition(self, employee_data):
        """Task 17: Create PredictAttrition function to accept employee data and predict stay/leave."""
        # employee_data should be a DataFrame or 2D array matching feature dimensions
        scaled_data = self.scaler.transform(employee_data)
        prediction = self.model.predict(scaled_data)
        return prediction

def main():
    # Initialize predictor system
    predictor = EmployeeAttritionPredictor('Assignment_62/Employee_Attrition.csv')
    
    # Run pipeline tasks
    try:
        predictor.load_and_explore_data()
    except FileNotFoundError:
        print("\n[Note]: 'Employee_Attrition.csv' was not found locally. Please ensure the CSV file is present in your working directory.")
        return

    predictor.preprocess_data()
    predictor.train_network()
    predictor.evaluate_model()

    print("\n--- 18. Testing the System with 5 New Employee Records ---")
    # Creating sample mock records mimicking the feature layout
    # Features order: Age, MonthlyIncome, YearsAtCompany, TotalWorkingYears, DistanceFromHome, 
    # JobSatisfaction, WorkLifeBalance, OverTime, NumCompaniesWorked, TrainingTimesLastYear
    sample_new_employees = pd.DataFrame([
        [29, 4500, 2, 5, 10, 3, 2, 1, 2, 2],
        [45, 12000, 10, 20, 2, 4, 3, 0, 1, 1],
        [24, 2500, 1, 1, 25, 1, 1, 1, 3, 3],
        [38, 8500, 6, 12, 5, 3, 3, 0, 2, 2],
        [31, 5100, 3, 7, 14, 2, 2, 1, 4, 1]
    ], columns=['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears', 
                'DistancefromHome', 'JobSatisfaction', 'WorkLifeBalance', 
                'OverTime', 'NumCompaniesWorked', 'TrainingTimesLastYear'])

    predictions = predictor.PredictAttrition(sample_new_employees)
    
    for i, pred in enumerate(predictions):
        status = "1 -> Employee is likely to leave" if pred == 1 else "0 -> Employee is likely to stay"
        print(f"Employee {i+1} Prediction: {status}")

if __name__ == "__main__":
    main()