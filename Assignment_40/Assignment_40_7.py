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
# 4. Predict Results for 5 New Students
# ============================================================

def predict_new_students(model):
    """
    Create a DataFrame containing five new students and use
    the trained model to predict whether they will pass or fail.
    """

    print("\n========== NEW STUDENT PREDICTIONS ==========")

    # Create data for five new students
    new_students = pd.DataFrame({
        "StudyHours": [6, 4, 8, 3, 7],
        "Attendance": [85, 72, 95, 60, 88],
        "PreviousScore": [66, 55, 82, 45, 75],
        "AssignmentsCompleted": [7, 5, 9, 3, 8],
        "SleepHours": [7, 6, 8, 5, 7]
    })

    # Predict the results
    predictions = model.predict(new_students)

    # Add predictions to DataFrame
    new_students["PredictedResult"] = predictions

    # Convert 1 and 0 into Pass and Fail
    new_students["Result"] = new_students["PredictedResult"].apply(
        lambda x: "Pass" if x == 1 else "Fail"
    )

    # Display predictions
    print(new_students)


# ============================================================
# 5. Calculate Accuracy Manually
# ============================================================

def calculate_manual_accuracy(y_test, y_pred):
    """
    Calculate classification accuracy manually without using
    sklearn's accuracy_score function and compare the result
    with sklearn accuracy.
    """

    print("\n========== MANUAL ACCURACY ==========")

    # Count the number of correct predictions
    correct = 0

    # Compare actual and predicted values
    for actual, predicted in zip(y_test, y_pred):

        if actual == predicted:
            correct += 1

    # Calculate total number of records
    total = len(y_test)

    # Calculate accuracy manually
    manual_accuracy = correct / total

    print("Correct predictions:", correct)
    print("Total predictions:", total)

    print(
        "Manual Accuracy:",
        round(manual_accuracy * 100, 2),
        "%"
    )

    # Calculate sklearn accuracy for verification
    sklearn_accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print(
        "Sklearn Accuracy:",
        round(sklearn_accuracy * 100, 2),
        "%"
    )

    # Verify both values
    if manual_accuracy == sklearn_accuracy:
        print("Both accuracy values match.")
    else:
        print("Accuracy values do not match.")


# ============================================================
# 6. Display Misclassified Students
# ============================================================

def display_misclassified_students(df, X_test, y_test, y_pred):
    """
    Identify students for whom the actual result and predicted
    result are different and display those records.
    """

    print("\n========== MISCLASSIFIED STUDENTS ==========")

    # Copy test data
    misclassified = X_test.copy()

    # Add actual values
    misclassified["ActualResult"] = y_test.values

    # Add predicted values
    misclassified["PredictedResult"] = y_pred

    # Identify incorrect predictions
    misclassified = misclassified[
        misclassified["ActualResult"] !=
        misclassified["PredictedResult"]
    ]

    # Display incorrect records
    print(misclassified)

    # Count misclassified students
    count = len(misclassified)

    print("\nNumber of misclassified students:", count)

    # Give a basic observation
    if count == 0:
        print("No students were misclassified.")
    else:
        print(
            "Misclassified students may have similar study, "
            "attendance or academic patterns despite having "
            "different final results."
        )


# ============================================================
# 7. Compare Different Random States
# ============================================================

def compare_random_states(df):
    """
    Train Decision Tree models using random_state values
    0, 10 and 42 and compare their testing accuracies.
    """

    print("\n========== RANDOM STATE COMPARISON ==========")

    # Select input features
    features = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[features]
    y = df["FinalResult"]

    # Random states to compare
    random_states = [0, 10, 42]

    # Train a model for every random state
    for state in random_states:

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=state
        )

        # Create model
        model = DecisionTreeClassifier(
            random_state=state
        )

        # Train model
        model.fit(X_train, y_train)

        # Predict test values
        predictions = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(
            y_test,
            predictions
        )

        print(
            "Random State:",
            state,
            "| Testing Accuracy:",
            round(accuracy * 100, 2),
            "%"
        )

    print(
        "\nObservation: Testing accuracy can change because "
        "different random states create different training "
        "and testing datasets."
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

    # ========================================================
    # Call Function 4
    # ========================================================

    predict_new_students(
        model
    )

    # ========================================================
    # Call Function 5
    # ========================================================

    calculate_manual_accuracy(
        y_test,
        y_pred
    )

    # ========================================================
    # Call Function 6
    # ========================================================

    display_misclassified_students(
        df,
        X_test,
        y_test,
        y_pred
    )

    # ========================================================
    # Call Function 7
    # ========================================================

    compare_random_states(
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