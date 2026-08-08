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


def analyze_study_hours_and_attendance(df):

    study_hours_result = df.groupby("FinalResult")["StudyHours"].mean()
    attendance_result = df.groupby("FinalResult")["Attendance"].mean()

    print("\nAverage StudyHours:")
    print(study_hours_result)

    print("\nAverage Attendance:")
    print(attendance_result)

    if study_hours_result.get(1, 0) > study_hours_result.get(0, 0):
        print("\nHigher StudyHours tend to increase the chance of passing.")
    else:
        print("\nHigher StudyHours do not clearly increase the chance of passing.")

    if attendance_result.get(1, 0) > attendance_result.get(0, 0):
        print("Higher Attendance tends to improve FinalResult.")
    else:
        print("Higher Attendance does not clearly improve FinalResult.")

    print("StudyHours and Attendance can be useful features for predicting student performance.")
    print("However, student performance depends on multiple factors.")


def plot_study_hours_histogram(df):

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["StudyHours"],
        bins=10,
        edgecolor="black"
    )

    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")

    plt.show()


def plot_study_hours_vs_previous_score(df):

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="StudyHours",
        y="PreviousScore",
        hue="FinalResult"
    )

    plt.title("StudyHours vs PreviousScore")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.show()


def plot_attendance_boxplot(df):

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        y=df["Attendance"]
    )

    plt.title("Attendance Boxplot")
    plt.ylabel("Attendance (%)")

    plt.show()

    q1 = df["Attendance"].quantile(0.25)
    q3 = df["Attendance"].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - (1.5 * iqr)
    upper_limit = q3 + (1.5 * iqr)

    outliers = df[
        (df["Attendance"] < lower_limit) |
        (df["Attendance"] > upper_limit)
    ]

    print("\nNumber of Attendance Outliers:", len(outliers))

    if len(outliers) > 0:
        print("Attendance outliers are present.")
        print(outliers[["Attendance"]])
    else:
        print("No Attendance outliers are present.")





def main():

    df = load_dataset()

    display_dataset_information(df)

    calculate_student_results(df)

    calculate_statistics(df)

    analyze_final_result_distribution(df)

    analyze_study_hours_and_attendance(df)

    plot_study_hours_histogram(df)

    plot_study_hours_vs_previous_score(df)

    plot_attendance_boxplot(df)




if __name__ == "__main__":
    main()