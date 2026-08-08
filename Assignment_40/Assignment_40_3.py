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
# 2. Remove SleepHours and Compare Accuracy
# ============================================================

def remove_sleep_hours(df, X_train, X_test, y_train, y_test,
                       original_accuracy):
    """
    Remove SleepHours from the dataset, train the Decision Tree
    again and compare its accuracy with the original model.
    """

    print("\n========== REMOVING SLEEP HOURS ==========")

    # Remove SleepHours from the feature list
    features_without_sleep = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"
    ]

    X = df[features_without_sleep]
    y = df["FinalResult"]

    # Split the new feature set
    X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create a new Decision Tree model
    model_without_sleep = DecisionTreeClassifier(
        random_state=42
    )

    # Train the model
    model_without_sleep.fit(X_train_new, y_train_new)

    # Make predictions
    predictions = model_without_sleep.predict(X_test_new)

    # Calculate accuracy
    new_accuracy = accuracy_score(
        y_test_new,
        predictions
    )

    print("Original accuracy:",
          round(original_accuracy * 100, 2), "%")

    print("Accuracy without SleepHours:",
          round(new_accuracy * 100, 2), "%")

    # Compare both accuracies
    if new_accuracy > original_accuracy:
        print("Removing SleepHours improved the performance.")
    elif new_accuracy < original_accuracy:
        print("Removing SleepHours reduced the performance.")
    else:
        print("Removing SleepHours did not change the performance.")

    return model_without_sleep


# ============================================================
# 3. Train Using StudyHours and Attendance
# ============================================================

def train_using_study_attendance(df):
    """
    Train a Decision Tree using only StudyHours and Attendance.
    Compare the model performance with the full-feature model.
    """

    print("\n========== STUDY HOURS + ATTENDANCE MODEL ==========")

    # Select only the required features
    X = df[["StudyHours", "Attendance"]]

    # Select target column
    y = df["FinalResult"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create Decision Tree model
    model = DecisionTreeClassifier(
        random_state=42
    )

    # Train the model
    model.fit(X_train, y_train)

    # Predict test values
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("Accuracy using StudyHours and Attendance:",
          round(accuracy * 100, 2), "%")

    print("\nObservation:")

    if accuracy >= 0.80:
        print(
            "The model is performing reasonably well using "
            "only StudyHours and Attendance."
        )
    else:
        print(
            "The model performance is lower with only "
            "StudyHours and Attendance."
        )

    return model


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

    # ========================================================
    # Call Function 2
    # ========================================================

    remove_sleep_hours(
        df,
        X_train,
        X_test,
        y_train,
        y_test,
        original_accuracy
    )

    # ========================================================
    # Call Function 3
    # ========================================================

    study_attendance_model = train_using_study_attendance(
        df
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