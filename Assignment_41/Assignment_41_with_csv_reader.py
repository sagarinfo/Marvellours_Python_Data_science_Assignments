

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


class WineClassifier:


    def __init__(self):
        self.data = None
        self.target = None
        self.feature_names = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        self.model = None
        self.predictions = None

    # ---------- Step 1 : Get Data ----------
    def get_data(self, Datapath):

        wine = pd.read_csv(Datapath)
        self.data = wine.drop(columns=['Class'])
        self.target = wine['Class']
        self.feature_names = wine.columns[:-1]

        print("Step 1 : Get Data")
        print(f"  Dataset shape : {self.data.shape}")
        print(f"  Classes present : {sorted(self.target.unique())}\n")
        return self.data, self.target

    # ---------- Step 2 : Clean, Prepare & Manipulate Data ----------
    def clean_prepare_data(self, test_size=0.3, random_state=42):
        missing_values = self.data.isnull().sum().sum()

        X_train, X_test, y_train, y_test = train_test_split(
            self.data, self.target,
            test_size=test_size,
            random_state=random_state,
            stratify=self.target
        )

        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(X_train)
        self.X_test = self.scaler.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test

        print("Step 2 : Clean, Prepare & Manipulate Data")
        print(f"  Missing values found : {missing_values}")
        print(f"  Training samples : {len(self.X_train)}")
        print(f"  Testing samples  : {len(self.X_test)}\n")
        return self.X_train, self.X_test, self.y_train, self.y_test

    # ---------- Step 3 : Train Model ----------
    def train_model(self):
        
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.model.fit(self.X_train, self.y_train)

        print("Step 3 : Train Model")
        print("  K-Nearest Neighbors Classifier trained successfully\n")
        return self.model

    # ---------- Step 4 : Test Data ----------
    def test_data(self):
        """Generate predictions for the test set."""
        self.predictions = self.model.predict(self.X_test)

        print("Step 4 : Test Data")
        print(f"  Predictions generated for {len(self.predictions)} samples")
        print(f"  Sample predictions : {list(self.predictions[:10])}\n")
        return self.predictions

    # ---------- Step 5 : Calculate Accuracy ----------
    def calculate_accuracy(self):
   
        accuracy = accuracy_score(self.y_test, self.predictions)

        print("Step 5 : Calculate Accuracy")
        print(f"  Accuracy : {accuracy * 100:.2f}%")
        print("\n  Confusion Matrix:")
        print(confusion_matrix(self.y_test, self.predictions))
        print("\n  Classification Report:")
        print(classification_report(self.y_test, self.predictions))
        return accuracy

    # ---------- Runs the full pipeline ----------
    def run(self):
    
        self.get_data("WinePredictor.csv")
        self.clean_prepare_data()
        self.train_model()
        self.test_data()
        return self.calculate_accuracy()


def main():
    classifier = WineClassifier()
    classifier.run()


if __name__ == "__main__":
    main()