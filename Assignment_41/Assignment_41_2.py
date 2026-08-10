

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
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
    def get_data(self):

        wine = load_wine()
        self.data = pd.DataFrame(wine.data, columns=wine.feature_names)
        self.target = pd.Series(wine.target, name="Class")
        self.feature_names = wine.feature_names

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


    # ---------- Runs the full pipeline ----------
    def run(self):
        """Execute the complete ML pipeline end to end."""
        self.get_data()
        self.clean_prepare_data()


def main():
    classifier = WineClassifier()
    classifier.run()


if __name__ == "__main__":
    main()