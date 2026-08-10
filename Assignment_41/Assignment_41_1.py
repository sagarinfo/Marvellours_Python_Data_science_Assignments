

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

    def run(self):
        self.get_data()


def main():
    classifier = WineClassifier()
    classifier.run()


if __name__ == "__main__":
    main()