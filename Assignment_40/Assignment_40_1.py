# ============================================================
# Student Performance Machine Learning Project
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


# ============================================================
# 1. Analyze Feature Importance
# ============================================================

def analyze_feature_importance(model, feature_names):
    """
    Display the importance of every feature used by the
    Decision Tree model and identify the most and least
    important features.
    """

    # Get feature importance values from the trained model
    importance = model.feature_importances_

    # Create a DataFrame for better display
    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    })

    # Sort features based on importance
    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\n========== FEATURE IMPORTANCE ==========")
    print(importance_df)

    # Find the most important feature
    most_important = importance_df.iloc[0]

    # Find the least important feature
    least_important = importance_df.iloc[-1]

    print("\nMost important feature:")
    print(
        most_important["Feature"],
        "->",
        round(most_important["Importance"], 4)
    )

    print("\nLeast important feature:")
    print(
        least_important["Feature"],
        "->",
        round(least_important["Importance"], 4)
    )


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    """
    Execute all ten machine learning tasks in sequence.
    """

    # --------------------------------------------------------
    # Load the dataset
    # --------------------------------------------------------

    df = pd.read_csv("student_performance_ml.csv")

    print("========== DATASET LOADED ==========")
    print(df.head())

    # --------------------------------------------------------
    # Prepare features and target
    # --------------------------------------------------------

    features = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[features]
    y = df["FinalResult"]

    # --------------------------------------------------------
    # Create training and testing datasets
    # --------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # --------------------------------------------------------
    # Create and train the main Decision Tree model
    # --------------------------------------------------------

    model = DecisionTreeClassifier(
        random_state=42
    )

    model.fit(X_train, y_train)

    # --------------------------------------------------------
    # Make predictions using the main model
    # --------------------------------------------------------

    y_pred = model.predict(X_test)

    # --------------------------------------------------------
    # Calculate original accuracy
    # --------------------------------------------------------

    original_accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print("\n========== ORIGINAL MODEL ==========")

    print(
        "Testing Accuracy:",
        round(original_accuracy * 100, 2),
        "%"
    )

    # ========================================================
    # Call Function 1
    # ========================================================

    analyze_feature_importance(
        model,
        features
    )


    # --------------------------------------------------------
    # Final message
    # --------------------------------------------------------

    print("\n======================================")
    print("All tasks completed successfully.")
    print("======================================")


# ============================================================
# Program execution
# ============================================================

if __name__ == "__main__":
    main()