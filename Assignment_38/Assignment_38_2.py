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


def main():

    df = load_dataset()

    display_dataset_information(df)

    calculate_student_results(df)



if __name__ == "__main__":
    main()