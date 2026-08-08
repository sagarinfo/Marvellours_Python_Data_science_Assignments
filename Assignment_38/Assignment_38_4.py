import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset():
    df = pd.read_csv("student_performance_ml.csv")
    return df


def display_dataset_information(df):

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nLast 5 Records:")
    print(df.tail())

    print("\nTotal Rows and Columns:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)


def calculate_student_results(df):

    total_students = len(df)

    passed_students = len(df[df["FinalResult"] == 1])

    failed_students = len(df[df["FinalResult"] == 0])

    print("\nTotal Number of Students:", total_students)
    print("Number of Passed Students:", passed_students)
    print("Number of Failed Students:", failed_students)


def calculate_statistics(df):

    average_study_hours = df["StudyHours"].mean()
    average_attendance = df["Attendance"].mean()
    maximum_previous_score = df["PreviousScore"].max()
    minimum_sleep_hours = df["SleepHours"].min()

    print("\nAverage StudyHours:", average_study_hours)
    print("Average Attendance:", average_attendance)
    print("Maximum PreviousScore:", maximum_previous_score)
    print("Minimum SleepHours:", minimum_sleep_hours)


def analyze_final_result_distribution(df):

    result_counts = df["FinalResult"].value_counts()

    print("\nFinalResult Distribution:")
    print(result_counts)

    total_students = len(df)

    passed_students = result_counts.get(1, 0)
    failed_students = result_counts.get(0, 0)

    pass_percentage = (passed_students / total_students) * 100
    fail_percentage = (failed_students / total_students) * 100

    print("\nPass Percentage:", round(pass_percentage, 2), "%")
    print("Fail Percentage:", round(fail_percentage, 2), "%")

    if pass_percentage >= 40 and fail_percentage >= 40:
        print("Dataset is reasonably balanced.")
    else:
        print("Dataset is imbalanced.")





def main():

    df = load_dataset()

    display_dataset_information(df)

    calculate_student_results(df)

    calculate_statistics(df)

    analyze_final_result_distribution(df)




if __name__ == "__main__":
    main()